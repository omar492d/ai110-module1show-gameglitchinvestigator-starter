# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| | | | | |
| | | | | |
| | | | | |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
Add professional grade docstrings to the functions in logic_utils.py. Also, review my code for PEP 8 style compliance.
```

**Linting output before:**

```
logic_utils.py — now PEP 8 clean. One note: line 71 except Exception: is broad (E722-adjacent style smell). Narrow to except ValueError: — that's what int/float raise.

app.py — only style issue: block comments need space after # (PEP 8 E265):

app.py:3 #FIX: → # FIX:
app.py:25 #FIX: → # FIX:
app.py:80 #FIX: → # FIX:
app.py:84 #st.session_state... → # st.session_state...
Rest clean. Line lengths fine. Want fixes applied?
```

**Changes applied:**

I applied the style suggestions. I also completely the removed the comment on app.py:84, as it served no purpose. Changed line 71 to except a value error.

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
