# Step 1
### Install gunicorn.
```bash
sudo apt-get update
sudo apt-get install gunicorn
```
### Usage example.
```bash
sudo gunicorn -w 2 -b :80 server:app
```
# Step 2
### Create configuration file.
