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
| Date  | Round  | Game | SoccerGPT Prediction | Final Score | Winner Correct | Score diff. correct | Score correct |
| ------ | ------| --- | ---------------------|--------------|----------------|---------------------|---------------|
| 06/14  | Group | Germany:Scotland  | 3:1  | 5:1            |       ✅︎       |        ❌           |       ❌       |
| 06/15  | Group | Hungary:Switzerland  | 1:2 | 1:3          |       ✅︎       |        ❌           |       ❌       |
| 06/15  | Group | Spain:Croatia  | 2:1 | 3:0                |       ✅︎       |        ❌           |       ❌       |
| 06/15  | Group | Italy:Albania  | 2:0 | 2:1                |       ✅︎       |        ❌           |       ❌       |
| 06/16  | Group | Poland:Netherlands  | 1:3 | 1:2           |       ✅︎       |        ❌           |       ❌       |
| 06/16  | Group | Slovenia:Denmark  | 1:2 | 1:1             |       ❌       |        ❌           |       ❌       |
| 06/16  | Group | Serbia:England  | 1:2 | 0:1               |       ✅︎       |        ✅︎           |       ❌       |
### Gameday 2
| Date  | Round  | Game | SoccerGPT Prediction | Final Score | Winner Correct | Score diff. correct | Score correct |
| ------ | ------| --- | ---------------------|--------------|----------------|---------------------|---------------|
| 06/17  | Group | Romania:Ukraine  | 2:1  | 3:0             |       ✅︎       |        ❌           |       ❌       |
| 06/17  | Group | Belgium:Slovakia  | 3:1 | 0:1             |       ❌       |       ❌            |       ❌       |
| 06/17  | Group | Austria:France  | 1:3 | 0:1               |       ✅︎       |        ❌           |       ❌       |
| 06/18  | Group | Turkey:Georgia  | 2:1 | 3:1               |       ✅︎       |        ❌           |       ❌       |
| 06/18  | Group | Portugal:Czech Republic  | 3:0 | 2:1      |       ✅︎       |        ❌           |       ❌       |
### Gameday 3
From here on out, we take stats from the current tournament into account.
| Date  | Round  | Game | SoccerGPT Prediction | Final Score | Winner Correct | Score diff. correct | Score correct |
| ------ | ------| --- | ---------------------|--------------|----------------|---------------------|---------------|
| 06/19  | Group | Croatia:Albania  | 1:1  | 2:2             |       ✅︎       |       ✅︎            |       ❌       |
| 06/19  | Group | Germany:Hungary  | 4:1 | 2:0              |       ✅︎       |       ❌            |       ❌       |
| 06/19  | Group | Scotland:Switzerland  | 1:3 | 1:1         |       ❌       |       ❌            |       ❌       |
| 06/20  | Group | Slovenia:Serbia  | 1:1 | 1:1              |       ✅︎       |       ✅︎            |       ✅︎       |
| 06/20  | Group | Denmark:England  | 1:2 | 1:1              |       ❌       |       ❌            |       ❌       |
| 06/20  | Group | Spain:Italy  | 2:1 | 1:0                  |       ✅︎       |       ✅︎            |       ❌       |
### Gameday 4
| Date  | Round  | Game | SoccerGPT Prediction | Final Score | Winner Correct | Score diff. correct | Score correct |
| ------ | ------| --- | ---------------------|--------------|----------------|---------------------|---------------|
| 06/21  | Group | Slovakia:Ukraine  | 2:0  | 1:2            |       ❌       |       ❌            |       ❌       |
| 06/21  | Group | Poland:Austria  | 1:2 | 1:3               |       ✅︎       |       ❌            |       ❌       |
| 06/21  | Group | Netherlands:France  | 1:2 | 0:0           |       ❌       |       ❌            |       ❌       |
| 06/22  | Group | Georgia:Czech Republic  | 1:2 | 1:1       |       ❌       |       ❌            |       ❌       |
| 06/22  | Group | Turkey:Portugal  | 1:3 | 0:3              |       ✅︎       |       ❌            |       ❌       |
| 06/22  | Group | Belgium:Romania  | 1:2 | 2:0              |       ❌       |       ❌            |       ❌       |
### Gameday 5
| Date  | Round  | Game | SoccerGPT Prediction | Final Score | Winner Correct | Score diff. correct | Score correct |
| ------ | ------| --- | ---------------------|--------------|----------------|---------------------|---------------|
| 06/23  | Group | Switzerland:Germany  | 1:3 | 1:1          |       ❌       |       ❌            |       ❌       |
| 06/23  | Group | Scotland:Hungary  | 1:2 | 0:1             |       ✅︎       |       ❌            |       ❌       |
| 06/24  | Group | Croatia:Italy  | 1:2 | 1:1                |       ❌       |       ❌            |       ❌       |
| 06/24  | Group | Albania:Spain  | 0:3 | 0:1                |       ✅︎       |       ❌            |       ❌       |
### Gameday 6
| Date  | Round  | Game | SoccerGPT Prediction | Final Score | Winner Correct | Score diff. correct | Score correct |
| ------ | ------| --- | ---------------------|--------------|----------------|---------------------|---------------|
| 06/25  | Group | Netherlands:Austria  | 2:1 | 2:3          |       ❌       |       ❌            |       ❌       |
| 06/25  | Group | France:Poland  | 3:0 | 1:1                |       ❌       |       ❌            |       ❌       |
| 06/25  | Group | Denmark:Serbia  | 2:1 | 0:0               |       ❌       |       ❌            |       ❌       |
| 06/25  | Group | England:Slovenia  | 2:0 | 0:0             |       ❌       |       ❌            |       ❌       |
### Gameday 7
| Date  | Round  | Game | SoccerGPT Prediction | Final Score | Winner Correct | Score diff. correct | Score correct |
| ------ | ------| --- | ---------------------|--------------|----------------|---------------------|---------------|
| 06/26  | Group | Ukraine:Belgium  | 1:3 | 0:0              |       ❌       |       ❌            |       ❌       |
| 06/26  | Group | Slovakia:Romania  | 1:2 | 1:1             |       ❌       |       ❌            |       ❌       |
| 06/26  | Group | Czech Republic:Turkey  | 1:2 | 1:2        |       ✅︎       |       ✅︎            |       ✅︎       |
| 06/26  | Group | Georgia:Portugal  | 0:3 | 2:0             |       ❌       |       ❌            |       ❌       |
### Best of 16
| Date  | Game | SoccerGPT Prediction | Final Score | Winner Correct | Score diff. correct | Score correct |
| ------ | ----| ---------------------- | ------------|----------------|---------------------|---------------|
| 06/29  |  Switzerland:Italy           | 5:6 | -     |       -        |        -            |       -       |
| 06/29  |  Germany:Denmark           | 2:0 | -       |       -        |        -            |       -       |
| 06/30  |  England:Slovakia           | 2:1 | -      |       -        |        -            |       -       |
| 06/30  |  Spain:Georgia           | 2:0 | -         |       -        |        -            |       -       |
| 07/01  |  France:Belgium           | 5:4 | -        |       -        |        -            |       -       |
| 07/01  |  Portugal:Slovenia        | 2:0 | -        |       -        |        -            |       -       |
| 07/02  |  Romania:Netherlands      | 1:2 | -        |       -        |        -            |       -       |
| 07/02  |  Austria:Turkey      | 2:1 | -             |       -        |        -            |       -       |



