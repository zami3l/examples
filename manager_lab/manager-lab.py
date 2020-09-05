#!/usr/bin/python3
# coding : utf-8

import argparse, logging, subprocess, os

def run_mode(args):

    if args['Mode'] == 'create':
        pull_img(args['Type'])
        create_lab(args['Name'], args['Type'], args['Number'])

    if args['Mode'] == 'start':
        start_lab(args['Name'])

    if args['Mode'] == 'stop':
        stop_lab(args['Name'])

    if args['Mode'] == 'delete':
        delete_lab(args['Name'])

def check_args(args):

    list_os = ('arch', 'debian', 'centos', 'alpine', 'ubuntu')
    list_mode = ('create', 'start', 'stop', 'delete')
    argsDefault = {'Mode': 'create', 'Type': 'debian', 'Name': 'LAB', 'Number': 1}

    # Check Type
    if not args.type:
            logging.info('The Type is empty. The default value is %s', argsDefault['Type'])
    elif args.type.lower() in list_os:
        argsDefault['Type'] = args.type.lower()        
    else:
        raise TypeError('The type is incorrect')
        
    logging.info('Type => %s', argsDefault['Type'])

    # Check Mode
    if args.mode.lower() in list_mode:
        argsDefault['Mode'] = args.mode.lower()
    else:
        raise TypeError('The mode is incorrect')
        
    logging.info('Mode => %s', argsDefault['Mode'])

    # Check Number
    if not args.number:
        logging.info('The number is empty. The default value is %s', argsDefault['Number'])
    elif args.number > 20:
        argsDefault['Number'] = 20
    else:
        argsDefault['Number'] = args.number

    logging.info('Number => %s', argsDefault['Number'])

    # Check Name
    if not args.name:
        logging.info('The name is empty. The default value is %s', argsDefault['Name'])
    else:
        argsDefault['Name'] = args.name

    return argsDefault

def pull_img(type):

    print("# Image recovery ({}) in progress.".format(type))

    cmd = subprocess.run(['docker', 'pull', type.lower()], 
                            stdout=subprocess.PIPE,
                            universal_newlines=True)

    logging.info(cmd.stdout)

    if not cmd.returncode :
        print('Image recovery is complete.')

def create_lab(name, type, number):

    for nb_container in range(number):

        print("# Create container : LAB_{}_{}".format(name, nb_container))

        cmd = subprocess.run(['docker', 'run', '-d', '--name', 'LAB_{}_{}'.format(name, nb_container), type], 
                            stdout=subprocess.PIPE,
                            universal_newlines=True)

    logging.info(cmd.stdout)

def start_lab(name):

    cmd = "docker ps -a --format='{{.Names}}' | grep '%s' | xargs docker start >/dev/null" % name
    os.system(cmd)
    logging.debug('Command start : \n %s', cmd)
    print('# Containers started.')

def stop_lab(name):

    cmd = "docker ps -a --format='{{.Names}}' | grep '%s' | xargs docker stop >/dev/null" % name
    os.system(cmd)
    logging.debug('Command stop : \n %s', cmd)
    print('# Containers stopped.')

def delete_lab(name):

        cmd = "docker ps -a --format='{{.Names}}' | grep '%s' | xargs docker rm >/dev/null 2>&1" % name
        os.system(cmd)
        logging.debug('Command delete : \n %s', cmd)
        print('# Containers delete.')

def main():

    # Init Logger
    logger = logging.getLogger()
    logging.basicConfig(format='%(levelname)s :: %(message)s')

    # Init Argparse
    parser = argparse.ArgumentParser(description='Script for the creation a lab of test')
    
    parser.add_argument('mode', type=str, metavar='MODE_LAB', help="Create / Start / Stop / Delete lab")
    parser.add_argument('-n', '--name', type=str, metavar='NAME_LAB', help="Lab name")
    parser.add_argument('-t', '--type', type=str, metavar='TYPE_LAB', help="Lab type (Debian, Arch, Centos, ...)")
    parser.add_argument('-nb', '--number', type=int, metavar='NUMBER', help="Number of machines that must be created")
    parser.add_argument('-v', '--verbose', action='store_true', help="Verbose mode")
    parser.add_argument('-d', '--debug', action='store_true', help="Debug mode")

    option = parser.parse_args()

    # Set logging
    if option.verbose:

        logger.setLevel(logging.INFO)

    if option.debug:

        logger.setLevel(logging.DEBUG)

    # Run
    run_mode(check_args(option))

if __name__ == "__main__":

    main()