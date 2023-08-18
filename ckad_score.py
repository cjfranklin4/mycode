import subprocess

def move_pod():
  try:
    # task 1: API primitives
    command = "kubectl get pod apricot -n banana"
    result = subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode == 0:
        return True
    else:
        print("Pod 'apricot' not found in namespace 'banana'")
        return False
  except:
      return False

def create_pod():
  try:
    # task 2: pod basics
    STATUS= True
    command = "kubectl get pod singer -n talent -o jsonpath='{.metadata.name}'"
    pod_name = subprocess.getoutput(command)
    if not pod_name:
        print("Pod 'singer' not found in namespace 'talent'.")
        STATUS= False

    command = "kubectl get pod singer -n talent -o jsonpath='{.spec.containers[*].name}'"
    container_name = subprocess.getoutput(command)
    if container_name != "opera":
        print("Container name is not 'opera'.")
        STATUS= False

    command = "kubectl get pod singer -n talent -o jsonpath='{.spec.containers[*].image}'"
    image = subprocess.getoutput(command)
    if image != "nginx:1.7.9":
        print("Image is not 'nginx:1.7.9'.")
        STATUS= False

    return STATUS
  except:
      return False

def deploy_history():
  try:
    # task 3: rollbacks
    DEPLOYMENT = "mufasa"
    NAMESPACE = "king-of-lions"

    command = f"kubectl get deployment {DEPLOYMENT} -n {NAMESPACE} -o jsonpath='{{.spec.replicas}}'"
    DESIRED_REPLICAS = int(subprocess.getoutput(command))
    command = f"kubectl get deployment {DEPLOYMENT} -n {NAMESPACE} -o jsonpath='{{.status.replicas}}'"
    CURRENT_REPLICAS = int(subprocess.getoutput(command))
    command = f"kubectl get deployment {DEPLOYMENT} -n {NAMESPACE} -o jsonpath='{{.status.availableReplicas}}'"
    AVAILABLE_REPLICAS = int(subprocess.getoutput(command))

    if DESIRED_REPLICAS == CURRENT_REPLICAS and DESIRED_REPLICAS == AVAILABLE_REPLICAS:
        return True
    else:
        print(f"Expected {DESIRED_REPLICAS} replicas, but found {CURRENT_REPLICAS} current replicas and {AVAILABLE_REPLICAS} available replicas for deployment '{DEPLOYMENT}' in namespace '{NAMESPACE}'.")
        return False
  except:
      return False

def configmap():
  try:
    # task 4: configmaps
    STATUS= False
    NAMESPACE = "metallica"
    CONFIGMAP = "metal-cm"
    DEPLOYMENT = "enter-sandman"

    # Check if the ConfigMap exists
    command = f"kubectl get configmap {CONFIGMAP} -n {NAMESPACE}"
    result = subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if result.returncode == 0:
        pass
    else:
        print(f"ConfigMap '{CONFIGMAP}' not found in namespace '{NAMESPACE}'.")
        exit(1)

    # Get the desired replica count for the deployment
    command = f"kubectl get deployment {DEPLOYMENT} -n {NAMESPACE} -o jsonpath='{{.spec.replicas}}'"
    DESIRED_REPLICAS = int(subprocess.getoutput(command))

    # Get the current running replica count for the deployment
    command = f"kubectl get deployment {DEPLOYMENT} -n {NAMESPACE} -o jsonpath='{{.status.availableReplicas}}'"
    AVAILABLE_REPLICAS = int(subprocess.getoutput(command))

    # Check if all replicas are up and running
    if DESIRED_REPLICAS == AVAILABLE_REPLICAS:
        STATUS= True
    else:
        print(f"Expected {DESIRED_REPLICAS} replicas, but found {AVAILABLE_REPLICAS} available replicas for deployment '{DEPLOYMENT}' in namespace '{NAMESPACE}'.")

    return STATUS
  except:
      return False


def security_context():
  try:
    # task 5: securitycontexts
    NAMESPACE = "fort-knox"
    POD_NAME = "gold-bar"

    # Check if the pod exists
    command = f"kubectl get pod {POD_NAME} -n {NAMESPACE}"
    result = subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode != 0:
        print(f"Pod '{POD_NAME}' not found in namespace '{NAMESPACE}'.")
        return False

    # Execute the 'id' command in the container
    command = f"kubectl exec {POD_NAME} -n {NAMESPACE} -- id"
    id_output = subprocess.getoutput(command)

    # Check the UID and GID
    if "uid=1000" in id_output and "gid=2000" in id_output:
        return True
    else:
        print(f"Pod '{POD_NAME}' in namespace '{NAMESPACE}' does not have the correct UID and GID (1000 and 2000).")
        return False
  except:
      return False

def log_check():
  try:
    # task 6: container logging
    file_path = "/home/student/mycode/lincoln-logs.txt"
    lines_to_check = [
        "10-listen-on-ipv6-by-default.sh: Getting the checksum of /etc/nginx/conf.d/default.conf",
        "10-listen-on-ipv6-by-default.sh: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf"
    ]

    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()

            for line in lines_to_check:
                if line not in file_contents:
                    print(f"The line '{line}' was not found in {file_path}.")
                    return False

            return True 

    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return False
  except:
      return False

def main():
    functions_to_check = [move_pod, create_pod, deploy_history, configmap, security_context, log_check]
    score = 0

    for task_num, func in enumerate(functions_to_check, start=1):
        result = func()
        if result:
            print("\033[92m" + f"Task {task_num} passed." + "\033[0m") # Green text
            score += 1
        else:
            print("\033[91m" + f"Task {task_num} failed." + "\033[0m") # Red text

    print(f"Final score: {score} out of {len(functions_to_check)}.")

if __name__ == "__main__":
    main()
