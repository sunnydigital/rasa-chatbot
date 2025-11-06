# Rasa Training Notes for Windows

## Known Issue: Windows Permission Error

When running `rasa train` on Windows, you may encounter a `PermissionError: [WinError 5] Access is denied` error. This is a known bug in Rasa's Windows path handling when using cached components.

## Workarounds

### Option 1: Use --force flag (Recommended for development)
```bash
rasa train --force
```
This forces Rasa to retrain all components without using the cache.

### Option 2: Clear cache before training
```bash
# Windows PowerShell
Remove-Item -Recurse -Force .rasa\cache

# Git Bash / WSL
rm -rf .rasa/cache

# Then run training
rasa train
```

### Option 3: Set environment variable
```bash
# Add this to your PowerShell profile or run before each training session
$env:TEMP = "C:\Temp"
# Make sure C:\Temp exists and has write permissions
```

## Current Model

The most recent working model is: `models/20251105-214000-warm-float.tar.gz`

## Running the Chatbot

To run the chatbot shell:
```bash
rasa shell
```

To run with the action server (when you have custom actions):
```bash
# Terminal 1
rasa run actions

# Terminal 2
rasa shell
```

## Configuration Summary

- **NLU Pipeline**: WhitespaceTokenizer, CountVectorsFeaturizer, DIETClassifier, FallbackClassifier
- **Policies**: MemoizationPolicy, RulePolicy, UnexpecTEDIntentPolicy, TEDPolicy
- **Intents**: ask_question, greet, goodbye, affirm, deny, mood_great, mood_unhappy, bot_challenge
- **Custom Action**: action_llama3_explain

## Deprecation Warnings (Can be ignored for now)

You may see warnings about:
- SQLAlchemy 2.0 compatibility
- pkg_resources deprecation
- JAX xla_computation

These warnings don't affect functionality but should be addressed in a future Rasa update.
