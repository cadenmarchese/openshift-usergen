import subprocess

# Gather user data
print("\nWELCOME TO USERGEN for OPENSHIFT 4\n")
user = input("Please enter desired username to add to cluster: ")
password = input("Please enter the password to be added to the user: ")


# Generate the htpasswd file (will not work if client is not linux, or if htpasswd not installed)
def generate_file():
    print("\nGENERATING THE HTPASSWD FILE...\n")
    subprocess.run(f"htpasswd -cib htpasswd {user} {password}", shell=True, stdout=None)


# Generate the secret
def create_secret():
    print("\nCREATING THE SECRET...\n")
    subprocess.run('oc create secret generic htpasswd-secret --from-file htpasswd -n openshift-config', shell=True)


# Edit the cluster oauth configuration
def edit_oauth():
    print("\nAPPLYING THE CONFIGURATION...\n")
    subprocess.run('oc create -f oauth.yaml', shell=True)


# Grant privileges, if desired.
def grant_admin():
    while True:
        admin = input("\nWould you like to grant this user cluster-admin? YES or NO: ")
        if admin == "NO":
            print("\nExiting...")
            exit(0)
        elif admin == "YES":
            subprocess.run(f'oc adm policy add-cluster-role-to-user cluster-admin {user}', shell=True)
            print("Done!")
            return
        else:
            print("Please enter YES or NO")


# run the stuff
generate_file()
create_secret()
edit_oauth()
grant_admin()
