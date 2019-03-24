# Encryption
How to use:
  1. Start terminal
  2. Select directory with files
  3. I) To encode(decode) you need input file, key and write command:
  
        python main.py encode(decode) [--cipher {caesar,vigenere,vernam}] [--key KEY]
               [--input-file INPUT_FILE] [--output-file OUTPUT_FILE]
        
     P.S. To vernam encode you need file with key

     II) To hack caesar cipher you need analysis data which you get using function "training" and write comman:
     
         python main.py hack [--cipher {caesar}]
               [--frequency_analysis-file FREQUENCY_ANALYSIS_FILE]
               [--input-file INPUT_FILE] [--output-file OUTPUT_FILE]
               
     III) To get analysis data you need big text(e.g. book) and write command:
     
         python main.py training [--cipher {caesar}] [--input-file INPUT_FILE]
               [--output-file OUTPUT_FILE]


In the folder "test" I put massage for encoding, key(for Vernam), Harry Potter for training and LOTR for hacking. 
