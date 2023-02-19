import paramiko
import scp

# Se connecter à la machine distante via SSH
ssh = paramiko.SSHClient()
sshset_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('adresse_ip_machine_distante', username='nom_utilisateur', password='mot_de_passe')

# Exécuter la commande d'arrêt de la machine distante
stdin, stdout, stderr = ssh.exec_command('sudo poweroff')

# Attendre que la machine soit éteinte
# Vous pouvez modifier le temps d'attente en fonction de votre système et de la vitesse de la connexion
time.sleep(60)

# Créer une connexion SCP pour récupérer les fichiers
client = scp.SCPClient(ssh.get_transport())

# Récupérer les fichiers de la machine distante vers la machine locale
# Vous devez remplacer les chemins d'accès locaux et distants par les vôtres
client.get('/chemin/fichier1', '/chemin/local/fichier1')
client.get('/chemin/fichier2', '/chemin/local/fichier2')

# Fermer la connexion SCP et SSH
client.close()
ssh.close()
