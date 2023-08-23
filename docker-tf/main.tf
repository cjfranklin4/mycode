/*
This is a multi line comment
*/
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.22.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "nginx" {
  name         = "nginx:1.19.6" //use nginx for out docker image
  keep_locally = true    // keep image after "destroy"
}

resource "docker_container" "nginx" {
  image = docker_image.nginx.image_id
  name  = "tutorial"
  ports { #have ngix up on these ports
    internal = 80
    external = 2224
  }
}

