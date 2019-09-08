# Move Downloads

This Python script is based on Kalle Hallden's [YouTube video](https://www.youtube.com/watch?v=qbW6FRbaSl0&t=200s)
to move the files downloaded with Google Chrome to the Downloads folder to
folders based on the file extension inside a new folder called "Descargas".

<span style="color:red">**IMPORTANT:**</span> It's important to note this script only works with downloads from
Google Chrome. If the script is running and another browser downloads a file,
most likely the download will fail.

## Python Environment

Conda was used to manage the environment. If you desire to use pip to download
the packages for the project just look at the `environment.yml` file for the
necessary packages.

### Create Conda Environment

To create the same environment with all the packages for that the script needs
run the following command in your CLI:
```
conda env create -f environment.yml
```

Verify the environment was created by checking that the environment `mv_dwnlds`
exists when running:
```
conda info -e
```

### Activating the Environment

To activate the environment execute in the CLI:
```
conda activate mv_dwnlds
```

## Running the Python Script

The script was made to be executed in the background. The Makefile included
has targets to run, stop or restart the sript in the background.

To run the script in the background with using the Makefile, make sure you're
inside the project directory where the Makefile is and execute:
```
make start
```

To stop the script in the background you can do:
```
make stop
```

To restart the script (`make stop` followed by `make start`) you can do:
```
make restart
```

