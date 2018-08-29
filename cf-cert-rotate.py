import time, os
import json
import hashlib
import yaml
import argparse

# how to install requirements - $ apt-get install python-yaml

# example
# python cert.py -o varstore/deployment-vars.yml.old -n varstore/deployment-vars.yml.new -r varstore/deployment-vars.yml -c addca

DEBUG=False

ADDCA_IGNORES=['diego_rep_agent_v2',"consul_agent","consul_server"]
REMOVECA_IGNORES=["consul_agent_ca"]
CONSULCA=["consul_agent_ca"]

def chk_cert(results, isca, oldfile, newfile, outname):
    oldstream = open(oldfile,'r')
    olddocs = yaml.load_all(oldstream)

    newstream = open(newfile,'r')
    newdocs = yaml.load_all(newstream)

    for newdoc in newdocs:
        continue
    for doc in olddocs:
        for k,v in doc.items():
            if type(v) == str:
                if v.find('-----BEGIN CERTIFICATE-----') >= 0:
                    print(k,v)
            elif type(v) == dict:
                if v.get('ca'):

                    ## Add ca and ca certificate
                    if isca == 'addca':
                        if v.get('ca') and not k in ADDCA_IGNORES:
                            print('-------must be old,new certificate orders-------', k)
                            try:
                                doc[k]['ca']= doc[k]['ca']+newdoc[k]['ca']
                                doc[k]['certificate']= doc[k]['certificate']+newdoc[k]['certificate']
                            except:
                                pass

                    elif isca == 'removeca':
                        if v.get('ca') and not k in REMOVECA_IGNORES:
                            print('-------must be new certificate and key-------', k)
                            try:
                                doc[k]['ca']= newdoc[k]['ca']
                                doc[k]['certificate']= newdoc[k]['certificate']
                                doc[k]['private_key']= newdoc[k]['private_key']
                            except:
                                pass
<<<<<<< HEAD
=======
                        elif v.get('ca'):
                            print('-------must be old,new certificate orders-------', k)
                            try:
                                doc[k]['ca']= doc[k]['ca']+newdoc[k]['ca']
                                doc[k]['certificate']= doc[k]['certificate']+newdoc[k]['certificate']
                            except:
                                pass
>>>>>>> removeca bug fix

                    elif isca == 'remove_consul_ca':
                        if v.get('ca') and k in CONSULCA:
                            print('-------must be new certificate and key-------', k)
                            try:
                                doc[k]['ca']= newdoc[k]['ca']
                                doc[k]['certificate']= newdoc[k]['certificate']
                                doc[k]['private_key']= newdoc[k]['private_key']
                            except:
                                pass


    with open(outname, 'w') as yaml_file:
        yaml_file.write( yaml.dump(doc, explicit_start=False,default_style='|'))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', default='ca', help='addca')
    parser.add_argument('-o', default='cert.yml.old', help='old file')
    parser.add_argument('-n', default='cert.yml.new', help='new file')
    parser.add_argument('-r', default='cert.yml', help='result file')
    results = parser.parse_args()
    chk_cert(results,results.c,results.o,results.n,results.r)

if __name__== "__main__":
  main()
