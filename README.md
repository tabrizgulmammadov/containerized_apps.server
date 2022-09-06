# Python Server


### How to run application as a container in your pc?
- Clone the project from master branch to you pc
- Go to the repository of the project and run 'docker build -t python-server .' command
- Check existing of created image named 'python-server' using 'docker images' command
- Enter 'docker run -i --net dotnetclient_default --name pserver-test python-server' in the terminal (powershell, command prompt, visual studio etc.)
- You can write any text for logging
