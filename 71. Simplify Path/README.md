# [71. Simplify Path](https://leetcode.com/problems/simplify-path/)

> **Difficulty:**  Medium

---

## 📝 Problem Description

Given a string `path`, which is an **absolute path** (starting with a slash `'/'`) to a file or directory in a Unix-style file system, simplify it. The simplified canonical path should:

- Start with a single slash `/`
- Eliminate multiple slashes (e.g., `"//"` becomes `"/"`)
- Remove any `"."` (current directory)
- Handle `".."` (parent directory) by going one level up (if possible)
- Ignore empty parts

Return the simplified canonical path.

---

## 🔍 Example

### Example 1
Input: path = "/home/"
Output: "/home"


### Example 2
Input: path = "/../"
Output: "/"


### Example 3
Input: path = "/a/./b/../../c/"
Output: "/c"


---

##  Constraints

- `1 <= path.length <= 3000`
- `path` consists of English letters, digits, period `'.'`, slash `'/'`, and underscores `'_'`.
- `path` is a valid absolute Unix-style path.

---

## Solution


1. **Split** the input path by `'/'` to get all components.
2. Use a **stack** (`simple_path`) to manage directory navigation:
   - If the component is `'..'`, pop from the stack (go back).
   - If it's a name (not empty or `'.'`), push it onto the stack.
3. Join the stack with `'/'` to build the canonical path.

---