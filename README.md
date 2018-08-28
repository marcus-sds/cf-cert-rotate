# cf-cert-rotate

## Download

    git clone https://github.com/marcus-sds/cf-cert-rotate.git
    sudo apt-get install python-yaml
    
## Rotate

1. Backup Current varstore file

1. Create New cert file with var-store options

1. add new ca

    python cf-cert-rotate.py -c **addca** -o [temp old certfile] -n [temp new certfile] -r [result certfile]
    
    > result_certfile should be varstore file when deploy cf

1. deploy CloudFoundry and Others

1. remove old ca

    python cf-cert-rotate.py -c **removeca** -o [temp old certfile] -n [temp new certfile] -r [result certfile]

    > result_certfile should be varstore file when deploy cf

1. deploy CloudFoundry again and Others

1. remove old consul ca

    python cf-cert-rotate.py -c **remove_consul_ca** -o [temp old certfile] -n [temp new certfile] -r [result certfile]

    > result_certfile should be varstore file when deploy cf

1. deploy CloudFoundry again and Others


## Issue

- Rep's tls had some issues when added new certificate to old ca certificate and when **addca**, it's excluded

