welcome to eco vision, a project to model global flood risk

to use the tiler

$source env/bin/activate
$cd tiler
place your target image in target_tif/proof.tif
$python tiler.py [x dimension] [y dimension]
your tiled tifs will now be located in tiled_tifs/




to start cvat 

$cd ~
$cd cvat
$sudo docker-compose up -d
if it looks like the server is running, create password
$sudo docker exec -it cvat bash -ic 'python3 ~/manage.py createsuperuser'

login at 

http://localhost:8080/

