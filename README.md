# sap

<p align="center">
  <a href="#"><img width="200px" src="https://github.com/leedaniil/sap/blob/master/application/sap/static/src/favicon.png" alt="sap"></a>
</p>

Students and Professors feedback system for improving and analyzing of education process at university

## Run a project

### Download a project.
```
git clone https://github.com/leedaniil/sap.git
cd sap/
```

Then, change `config.json`: 
- You need to get a Telegram token for your Telegram Bot and replace it in `config.json`;
- Set `true` or `false` for "prod" in `config.json`;

### Run/clean in local environment
```
make init
make run

make clean
```

### Run/clean in Docker
```
make docker

make docker-clean
```

## Generate fake data
```
make fake-gen
```
