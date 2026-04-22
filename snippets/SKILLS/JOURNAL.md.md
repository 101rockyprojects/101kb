```m̀arkdown
--- name: journal description: Creates and maintains a JOURNAL.md file in the root of the project to keep crucial information about your project, keeping notes in *JOURNAL.md* of problems, conclusions, questions, what the plan is, and tick off tasks as you finish them. --- **Prompt:** You are an expert engineer. Your task is to implement **Task X** (describe Task X here). You **must** maintain a file named `JOURNAL.md` throughout the implementation. Use it to track progress, record issues, capture decisions, and plan next steps. ### **Mandatory format for JOURNAL.md:**``

# JOURNAL.md

## ✅ Task Tracking

- Task description (pending)
    
- Completed task description
    

## ❌ Problems Encountered

- Problem description + how it was fixed (or needs fixing)
    

## 💡 Conclusions & Decisions

- What you learned, why you chose approach A over B
    

## ❓ Open Questions

- Anything unclear, needs clarification, or blocked by external factors
    

## 📋 Next Steps

- Immediate actions to continue implementation
    


### **Rules you must follow:**

1. **Before coding** – Create `JOURNAL.md` with the initial plan under `📋 Next Steps` and list all known tasks under `✅ Task Tracking`.

2. **During implementation** –
   - Tick off tasks as you finish them (`[x]`).
   - If you hit a problem, log it under `❌ Problems` and note how you fixed it.
   - If you find something that needs fixing but **isn't part of your assignment**, write it in `❌ Problems` or `💡 Conclusions` and **continue with your assignment** – do not derail.

3. **After each work session** – Update `📋 Next Steps` with what to do next.

4. **Use persistent memory beads** – Treat `JOURNAL.md` as your external memory. Always read it before starting work and append to it during work.

5. **When you finish Task X completely** –
   - Mark all tasks as `[x]`.
   - Write a final `💡 Conclusion` summarizing the implementation.
   - List any leftover `❓ Open Questions` for future work.

6. **When editing JOURNAL.md**
   - Any change in this file has to be prefixed by '//'.
   - Any line prefixed with '//' in this file has to be ignored.
```