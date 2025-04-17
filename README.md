# VolleyballStats2

Second version for calculating stats. This version utilizes user inputs from the command line. Run the main.py file to start the program. 

The program will prompt the user for:
- Players = Player Name and Number
  - The **number** can only be within **0-99** 
- Quality values = Perfect, Good, Ok, Poor, Error
  - The **value** can only be within **0-99**   
- Action alias = Serve, Serve Receive Pass, Free Ball Pass, Dig, Set, Attack, Block
  - The **alias** can only be a single character **a-z** 
- Raw Data File = Relative file path from main directory
  - Use relative path from the main directory for best results

**NOTE** - You can add your raw data file into the *data/raw_stats* folder in the main directory and then use that folder location as a relative file path.
Eg. /data/raw_stats/test.txt is what you will input when prompted for the raw stat file

**NOTE** - This program will only work if the raw stats file is formatted in a specific way. The format must be a stat per line and in the following format:
```
<player number> <action alias> <quality value>
```
Remember the player number and quality value should be between 0-99 and the action alias should be a single character between a-z.

The output files will be under *data/clean_stats* and *data/results*. 
The *clean_stats* folder holds the cleaned version of your raw stat files. 
The *results* folder holds the final results of each raw stat file and a total file for all raw stat files inputted.
