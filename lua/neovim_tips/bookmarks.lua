---@class NeovimTipsBookmarks
---Bookmark management functionality for saving and retrieving favorite tips
local M = {}

---@class BookmarkData
---@field bookmarks string[] Array of bookmarked tip titles

---Get the path to the bookmarks file
---@return string path Path to bookmarks JSON file
local function get_bookmarks_file()
  return vim.fn.stdpath("data") .. "/neovim_tips/bookmarks.json"
end

---Read bookmarks from persistent storage
---@return string[] bookmarks Array of bookmarked tip titles
local function read_bookmarks()
  local bookmarks_file = get_bookmarks_file()
  local file = io.open(bookmarks_file, "r")
  if not file then
    return {}
  end

  local content = file:read("*all")
  file:close()

  local ok, data = pcall(vim.json.decode, content)
  if ok and data and data.bookmarks then
    return data.bookmarks
  end

  return {}
end

---Write bookmarks to persistent storage
---@param bookmarks string[] Array of tip titles to save
---@return nil
local function write_bookmarks(bookmarks)
  local bookmarks_file = get_bookmarks_file()
  local data = { bookmarks = bookmarks }

  -- Ensure directory exists
  local dir = vim.fn.fnamemodify(bookmarks_file, ":h")
  vim.fn.mkdir(dir, "p")

  local file = io.open(bookmarks_file, "w")
  if file then
    file:write(vim.json.encode(data))
    file:close()
  end
end

-- Cache for bookmarks to avoid file I/O on every check
local bookmarks_cache = nil

---Load bookmarks into cache
---@return nil
local function load_bookmarks_cache()
  if not bookmarks_cache then
    bookmarks_cache = {}
    local bookmarks = read_bookmarks()
    for _, title in ipairs(bookmarks) do
      bookmarks_cache[title] = true
    end
  end
end

---Save bookmarks cache to file
---@return nil
local function save_bookmarks_cache()
  if bookmarks_cache then
    local bookmarks = {}
    for title, _ in pairs(bookmarks_cache) do
      table.insert(bookmarks, title)
    end
    table.sort(bookmarks)
    write_bookmarks(bookmarks)
  end
end

---Check if a tip is bookmarked
---@param title string The tip title to check
---@return boolean is_bookmarked True if tip is bookmarked
function M.is_bookmarked(title)
  load_bookmarks_cache()
  return bookmarks_cache[title] == true
end

---Add a tip to bookmarks
---@param title string The tip title to bookmark
---@return nil
function M.add_bookmark(title)
  if not title or title == "" then
    return
  end
  
  load_bookmarks_cache()
  bookmarks_cache[title] = true
  save_bookmarks_cache()
end

---Remove a tip from bookmarks
---@param title string The tip title to unbookmark
---@return nil
function M.remove_bookmark(title)
  if not title or title == "" then
    return
  end
  
  load_bookmarks_cache()
  bookmarks_cache[title] = nil
  save_bookmarks_cache()
end

---Toggle bookmark status for a tip
---@param title string The tip title to toggle
---@return boolean new_status New bookmark status after toggle
function M.toggle_bookmark(title)
  if M.is_bookmarked(title) then
    M.remove_bookmark(title)
    return false
  else
    M.add_bookmark(title)
    return true
  end
end

---Get all bookmarked tip titles
---@return string[] bookmarks Array of bookmarked tip titles
function M.get_bookmarks()
  load_bookmarks_cache()
  local bookmarks = {}
  for title, _ in pairs(bookmarks_cache) do
    table.insert(bookmarks, title)
  end
  table.sort(bookmarks)
  return bookmarks
end

---Clear all bookmarks
---@return nil
function M.clear_all_bookmarks()
  bookmarks_cache = {}
  save_bookmarks_cache()
end

---Get count of bookmarked tips
---@return integer count Number of bookmarked tips
function M.get_bookmark_count()
  load_bookmarks_cache()
  local count = 0
  for _, _ in pairs(bookmarks_cache) do
    count = count + 1
  end
  return count
end

---Calculate similarity between two strings using Levenshtein-like approach
---@param str1 string First string
---@param str2 string Second string
---@return number similarity Similarity score (0-1, higher is more similar)
local function calculate_similarity(str1, str2)
  str1 = str1:lower()
  str2 = str2:lower()

  if str1 == str2 then
    return 1.0
  end

  -- Check if one contains the other
  if str1:find(str2, 1, true) or str2:find(str1, 1, true) then
    return 0.8
  end

  -- Simple word overlap scoring
  local words1 = {}
  for word in str1:gmatch("%w+") do
    words1[word] = true
  end

  local words2 = {}
  for word in str2:gmatch("%w+") do
    words2[word] = true
  end

  local common = 0
  local total = 0
  for word in pairs(words1) do
    total = total + 1
    if words2[word] then
      common = common + 1
    end
  end
  for word in pairs(words2) do
    if not words1[word] then
      total = total + 1
    end
  end

  if total == 0 then
    return 0
  end

  return common / total
end

---Find the most similar tip title from available titles
---@param target_title string Title to find similar match for
---@param available_titles string[] List of available tip titles
---@param min_similarity number Minimum similarity threshold (0-1)
---@return string|nil best_match Most similar title, or nil if none above threshold
local function find_similar_title(target_title, available_titles, min_similarity)
  local best_match = nil
  local best_score = min_similarity or 0.7

  for _, title in ipairs(available_titles) do
    local score = calculate_similarity(target_title, title)
    if score > best_score then
      best_score = score
      best_match = title
    end
  end

  return best_match
end

---Validate bookmarks against currently loaded tips and fix orphaned bookmarks
---Tries to find similar tips for bookmarks that no longer exist
---@param available_titles string[] List of currently available tip titles
---@return table validation_result Information about validation and updates
function M.validate_bookmarks(available_titles)
  load_bookmarks_cache()

  -- Build set of available titles for fast lookup
  local available_set = {}
  for _, title in ipairs(available_titles) do
    available_set[title] = true
  end

  local result = {
    total_bookmarks = 0,
    valid_bookmarks = 0,
    orphaned_bookmarks = 0,
    redirected_bookmarks = 0,
    removed_bookmarks = 0,
    updates = {}  -- List of {old_title, new_title, action}
  }

  local updated_cache = {}

  for old_title, _ in pairs(bookmarks_cache) do
    result.total_bookmarks = result.total_bookmarks + 1

    if available_set[old_title] then
      -- Bookmark is still valid
      updated_cache[old_title] = true
      result.valid_bookmarks = result.valid_bookmarks + 1
    else
      -- Bookmark points to non-existent tip
      result.orphaned_bookmarks = result.orphaned_bookmarks + 1

      -- Try to find a similar tip
      local similar_title = find_similar_title(old_title, available_titles, 0.7)

      if similar_title then
        -- Found a similar tip - redirect bookmark
        updated_cache[similar_title] = true
        result.redirected_bookmarks = result.redirected_bookmarks + 1
        table.insert(result.updates, {
          old_title = old_title,
          new_title = similar_title,
          action = "redirected"
        })
      else
        -- No similar tip found - remove bookmark
        result.removed_bookmarks = result.removed_bookmarks + 1
        table.insert(result.updates, {
          old_title = old_title,
          new_title = nil,
          action = "removed"
        })
      end
    end
  end

  -- Update bookmarks cache if changes were made
  if result.redirected_bookmarks > 0 or result.removed_bookmarks > 0 then
    bookmarks_cache = updated_cache
    save_bookmarks_cache()
  end

  return result
end

return M