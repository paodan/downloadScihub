# downloadScihub
Download papers from Sci-Hub (https://sci-hub.se/) using python3, please ensure the Python3 has been installed before running the following code.

Suppose you would like to download the following papers:

"Concise Review: MSC-Derived Exosomes for Cell-Free Therapy"

"MSC exosome works through a protein-based mechanism of action"

"Mammalian MSC from selected species: Features and applications"

"Error paper name"


In the terminal input the following command:

```
./downloadScihub.py 'https://sci-hub.se/' "Concise Review: MSC-Derived Exosomes for Cell-Free Therapy" "MSC exosome works through a protein-based mechanism of action" "Mammalian MSC from selected species: Features and applications" "Error paper name"
```

Then the first 3 papers will be downloaded into your current directory and the "Error paper name" will be written in the log.txt file.



