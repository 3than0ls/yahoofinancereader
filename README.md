# Yahoo Finance CSV Sheet Interpreter

## My AP Econ teacher created a stock project, and a requirement is a lot of data collection. This simplifies the whole process with one button.

To get this working, simply download repo (blah blah blah), then navigate to [Yahoo Finance](https://finance.yahoo.com/). Pick whatever stock you want. My example is [Lockheed Martin](https://finance.yahoo.com/quote/LMT?p=LMT). Afterwards, click **Historical Data** on the bar. For the example, it would take me to [Lockheed Martin's Historical Data](https://finance.yahoo.com/quote/LMT/history?p=LMT). Next, click download. A CSV file with the stock's ticker name will be downloaded.

After downloading any number of CSV files, place them all in the `/data` folder in this repository. If it doesn't exist, create it, because this is where the script will read CSV files from.

Run the script, and in the `/output` folder, two output files will be generated. One, `output.txt`, is for general "easy to look at" data, while `output_specialized.txt` is specialized to be used in my AP Econ teacher's project.

To specify parameters, sadly there's no command line implementation. Go into `main.py` and edit `START_DATE` and `CUTOFF` variables.
