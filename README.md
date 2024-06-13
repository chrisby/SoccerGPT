# SoccerGPT

Using OpenAI's `GPT-4o` and the [Sportmonks Football API](https://www.sportmonks.com/football-apis) to predict match winners of the 2024 European Soccer Championship. Take a look at the [notebook outputs](https://github.com/chrisby/SoccerGPT/blob/main/main.ipynb) to see the predicted winner! 

The LLM receives team performance statistics from the 2024 qualification tournament as well as detailed player statistics.

## Get your own predictions
1. Insert you OpenAI key in the second cell of the notebook
2. Set your sportmonks token in `line 6` of `helper.py`. To get results, sign up for the `EURO 2024` plan which includes the qualification statistics.
3. Update prompts throughout the code base if required.

## Code quality
This is a POC hacked together over a couple hours, so I can submit my predictions to my betting platform, don't judge ;).  
