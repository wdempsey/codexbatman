# Examples: Causal Design Check

## Example 1

User request:

> Run a causal design check for our DiD policy analysis before we estimate effects.

Expected behavior:

- define estimand precisely
- enumerate parallel-trends and timing assumptions
- document threats and interpretation limits

Expected artifacts:

- causal design check artifact
- assumptions and threat register
- proceed/halt recommendation

## Example 2

User request:

> We have treatment and control groups; verify whether overlap and interference are acceptable.

Expected behavior:

- specify overlap diagnostics
- assess potential spillovers
- define sensitivity checks

Expected artifacts:

- overlap/support assessment plan
- interference risk notes
- recommendation with conditions

## Example 3 (Bad Invocation)

User request:

> Just tell me if this proves causality.

Expected Codex response:

- refuse binary proof framing
- require estimand and design assumptions
- return structured causal design checklist before conclusions

Expected artifacts after correction:

- estimand definition
- assumptions/threats section
- interpretation limits section
