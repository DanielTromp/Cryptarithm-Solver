# Cryptarithm-Solver
Cryptarithm Solver for resolving cryptopuzzles
> Performance python 100,000 calculations per second
> Performance pypy3  250,000 calculations per second

## Running the decoder with docker

**Option 1, pull and run the code in one line:**
*The code will run in Jupyter*
```
docker run -p 8888:8888 danieltromp/decoder-pypy
```

**Option 2, git download the code and build:**
*The code will run in Jupyter*
```
git clone https://github.com/DanielTromp/Cryptarithm-Solver.git
cd Cryptarithm-Solver
docker build -t decoder-pypy .
docker run -p 8888:8888 decoder-pypy
```

**Option 3, git download the script and run it from terminal:**
*The python script runs from terminal*
```
git clone https://github.com/DanielTromp/Cryptarithm-Solver.git
cd Cryptarithm-Solver
python dt-cryptarithm-solver.py
```
