import paramiko
import scp
from selenium import webdriver

# Se connecter à la machine distante via SSH
ssh = paramiko.SSHClient()
sshset_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('adresse_ip_machine_distante', username='nom_utilisateur', password='mot_de_passe')

# Exécuter la commande d'arrêt de la machine distante
stdin, stdout, stderr = ssh.exec_command('shutdown -s')

# Attendre que la machine soit éteinte
# Vous pouvez modifier le temps d'attente en fonction de votre système et de la vitesse de la connexion
time.sleep(60)

# Créer une connexion SCP pour récupérer les fichiers
client = scp.SCPClient(ssh.get_transport())

# Récupérer les fichiers de la machine distante vers la machine locale
# Vous devez remplacer les chemins d'accès locaux et distants par les vôtres
client.get('/chemin/fichier1', '/chemin/local/fichier1')
client.get('/chemin/fichier2', '/chemin/local/fichier2')

#dans ce code nous voulons ouvrir le navigateur chrome
# URL de la machine distante
remote_url = "http://<adresse-ip-de-la-machine-distante>:<port>/wd/hub"

# Options de configuration de Chrome pour la machine distante
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--headless')

# Initialisation du navigateur sur la machine distante
browser = webdriver.Remote(command_executor=remote_url, options=chrome_options)

# Ouvrir Google Chrome
browser.get("https://www.google.com")

# Fermer le navigateur
browser.quit()

# Fermer la connexion SCP
client.close()

# Fermer la connexion SCP
ssh.close()
