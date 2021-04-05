# Move Downloads

Project that takes [@KalleHallden](https://github.com/KalleHallden)'s Python automation shown in this [YouTube video](https://www.youtube.com/watch?v=qbW6FRbaSl0&t=200s)
to move the files downloaded with Google Chrome or Safari from the Downloads folder into folders based on the file extension inside a new specified folder.

And runs it in the background as an agent on user log in using macOS' launchd.

## Installation

**Step 1:**
Clone master branch or download the latest release.

**Step 2:**
Once you have cloned the repo or downloaded the release, create a Python environment and install the packages needed.

### Python Environment w/ Anaconda

The repo has an `environment.yml` file to create a Python environment called `mv_dwnlds` and install all packages.

To create environment and install packages run:

```bash
conda env create -f environment.yml
```

or

### Python Envrionment w/ Pip

If you used another method to create the Python environment that uses pip to manage packages, the repo also has a `requirements.txt` file with the packages needed.

To install packages with pip run:

```bash
pip install -r requirements.txt
```

**Step 3:**
Setup config file.

Rename the `emtpy-config.yml` file to `config.yml`:

```bash
mv empty-config.yml config.yml
```

Open the `config.yml` file and fill in the config values using absolute paths. 

As an **example** here's what my `config.yml` file looks like:

```yaml
##                    ##
# Download dirs config #
##                    ##

# Path to default downloads directory
track_dir: /Users/pablordoricaw/Downloads/

# Path to new download directory where downloads will be moved to
dst_dir: /Users/pablordoricaw/Descargas/

# Files that will not be moved from default downloads directory
ignore_files:
  - README!.txt
  - .DS_Store

##                  ##
# macOS Agent config #
##                  ##

# Path to User's Launch Agent's dir to load agent when user logs in
launch_agent_dir: /Users/pablordoricaw/Library/LaunchAgents/

# Agent name to find when checking if running
plist_name: local.user.mv_dwnlds

python_env: /Users/pablordoricaw/anaconda3/envs/mv_dwnlds/bin/python
```

Optional: The config value, ignore_files, can be ignored or you can chose to move the
`README!.txt` file to your original Downloads folder to remind you of where the
downloads are going in case you forget.

## Usage

**Step 1:**
Activate the environment created.

### Activate environment w/ Anaconda

If you created the environment with Anaconda and didn't change the name of the env in the first line of the `environment.yml` file, then run:

```bash
conda activate mv_dwnlds
```

**Step 2:**
Load agent.

Once the Python environment is active.

### Run w/ make

The project can be run with `make` by running:

```bash
make load
```

or

### Run Python script directly

To run:

```bash
python mv_dwnlds/plist.py -l
```

## Uninstall

**Step 1:** Unload agent.

### Unload w/ make

Unload:

```bash
make unload
```

or

### Unload w/ Python script

To unload:

```bash
python mv_dwnlds/plist.py -u
```

**Step 2:** Delete plist file.

### Delete plist file w/ make

```bash
make rm
```

#### Delete plist file w/ Python script

```bash
python mv_dwnlds/plist.py --rm
```

**Step 3:** Delete the project folder.
