<p align="center">
  <img src="https://raw.githubusercontent.com/chrisby/SoccerGPT/main/logo.webp" alt="drawing" width="200"/>
</p>

# SoccerGPT
Using OpenAI's `GPT-4o` and the [Sportmonks Football API](https://www.sportmonks.com/football-apis) to predict match winners of the 2024 European Soccer Championship. Take a look at the [notebook outputs](https://github.com/chrisby/SoccerGPT/blob/main/main.ipynb) to see the predicted winner! 

The LLM receives team performance statistics from the 2024 qualification tournament as well as detailed player statistics.

## Get your own predictions
1. Insert you OpenAI key in the second cell of the notebook
2. Set your sportmonks token in `line 6` of `helper.py`. To get results, sign up for the `EURO 2024` plan which includes the qualification statistics.
3. Update prompts throughout the code base if required.
4. To include statistics from the tournament as soon as results are available, update [this line](https://github.com/chrisby/SoccerGPT/blob/main/helper.py#L309).

## Code quality
This is a POC hacked together over a couple hours, so I can submit my predictions to my betting platform, don't judge ;).

## Predictions
Predictions will be updated throughout the tournament.
### Gameday 1
| Date  | Round  | Game | SoccerGPT Prediction | Final Score |
| ------ | ------| --- | ---------------------|--------------|
| 06/14  | Group | Germany:Scotland  | 3:1  | 5:1 |
| 06/15  | Group | Hungary:Switzerland  | 1:2 | 1:3 |
| 06/15  | Group | Spain:Croatia  | 2:1 | 3:0 |
| 06/15  | Group | Italy:Albania  | 2:0 | 2:1 |
| 06/16  | Group | Poland:Netherlands  | 1:3 | 1:2 |
| 06/16  | Group | Slovenia:Denmark  | 1:2 | - |
| 06/16  | Group | Serbia:England  | 1:2 | - |
### Gameday 2
| Date  | Round  | Game | SoccerGPT Prediction | Final Score |
| ------ | ------| --- | ---------------------|--------------|
| 06/17  | Group | Romania:Ukraine  | 2:1  | - |
| 06/17  | Group | Belgium:Slovakia  | 3:1 | - |
| 06/17  | Group | Austria:France  | 1:3 | - |
| 06/18  | Group | Turkey:Georgia  | 2:1 | - |
| 06/18  | Group | Portugal:Czech Republic  | 3:0 | - |
### Gameday 3
| Date  | Round  | Game | SoccerGPT Prediction | Final Score |
| ------ | ------| --- | ---------------------|--------------|
| 06/19  | Group | Croatia:Albania  | 1:2  | - |
| 06/19  | Group | Germany:Hungary  | 3:1 | - |
| 06/19  | Group | Scotland:Switzerland  | 1:3 | - |
| 06/20  | Group | Slovenia:Serbia  | TBD | - |
| 06/20  | Group | Denmark:England  | TBD | - |
| 06/20  | Group | Spain:Italy  | 2:1 | - |
