-- Test script to demonstrate bookmark validation
-- This shows how the validation works when tips are removed
-- Run from plugin root: nvim -l tests/test_bookmark_validation.lua

-- Add the lua directory to package path
package.path = "./lua/?.lua;./lua/?/init.lua;" .. package.path

local bookmarks = require("neovim_tips.bookmarks")

-- Simulate some bookmarked tips before deduplication
local test_bookmarks = {
  "Alternative Escape Key Mappings",  -- This was removed as duplicate
  "Quick Escape from Insert Mode",    -- This was removed as duplicate
  "Quick Escape Key Alternatives in Insert Mode",  -- This was kept (longest)
  "Navigate Between Buffers",         -- This still exists
}

-- Add test bookmarks to the system
print("=== Bookmark Validation Test ===\n")
print("Setting up test bookmarks...")
for _, title in ipairs(test_bookmarks) do
  bookmarks.add_bookmark(title)
end

print("Bookmarks before validation:")
for i, title in ipairs(test_bookmarks) do
  print(string.format("  %d. %s", i, title))
end

-- Simulate available titles after deduplication
local available_titles = {
  "Quick Escape Key Alternatives in Insert Mode",  -- Kept version
  "Navigate Between Buffers",
  "Use Marks for Quick Navigation",
  "Search and Replace Patterns",
  -- Note: the other two escape key tips were removed
}

print("\nAvailable tips after deduplication:")
for i, title in ipairs(available_titles) do
  print(string.format("  %d. %s", i, title))
end

print("\n--- Running validation ---\n")

local result = bookmarks.validate_bookmarks(available_titles)

print(string.format("Total bookmarks: %d", result.total_bookmarks))
print(string.format("Valid bookmarks: %d", result.valid_bookmarks))
print(string.format("Orphaned bookmarks: %d", result.orphaned_bookmarks))
print(string.format("Redirected bookmarks: %d", result.redirected_bookmarks))
print(string.format("Removed bookmarks: %d", result.removed_bookmarks))

if #result.updates > 0 then
  print("\nBookmark updates:")
  for _, update in ipairs(result.updates) do
    if update.action == "redirected" then
      print(string.format("  ✓ Redirected: '%s'", update.old_title))
      print(string.format("    → '%s'", update.new_title))
    elseif update.action == "removed" then
      print(string.format("  ✗ Removed: '%s' (no similar tip found)", update.old_title))
    end
  end
end

print("\n=== Expected Behavior ===")
print("1. 'Navigate Between Buffers' - stays valid (exact match)")
print("2. 'Quick Escape Key Alternatives...' - stays valid (exact match)")
print("3. 'Alternative Escape Key Mappings' - removed (similarity < 70%)")
print("4. 'Quick Escape from Insert Mode' - removed (similarity < 70%)")
print("\nNote: Word-overlap algorithm requires 70% similarity for redirection.")

-- Clean up test bookmarks
print("\n--- Cleaning up test bookmarks ---")
bookmarks.clear_all_bookmarks()
print("Test complete!")
