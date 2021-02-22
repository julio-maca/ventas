import click

from clients.services import ClientService
from clients.models import Client

@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass

@clients.command()
@click.option('-n', '--name',
                type=str,
                prompt=True,
                help='the client name')


@click.option('-c', '--company',
                type=str,
                prompt=True,
                help='the client company')


@click.option('-e', '--email',
                type=str,
                prompt=True,
                help='the client email')


@click.option('-p', '--position',
                type=str,
                prompt=True,
                help='the client position')


@click.pass_contex
def create(ctx, name, company, email, position):
    """Creeatre a new client"""
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj ['client_table'])

    client_service.create_client(client)

@clients.command()
@click.pass_contex
def list(ctx):
    """List all clients"""
    client_service = ClientService(ctx.obj['clients_table']) 
    client_list = client_service.list_clients()

    click.echo(' ID | NAME | COMPANY | EMAIL | PSITION')
    click.echo('*'*100)

    for client in client_list:
        click.echo('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=client['uid'],
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))

@clients.command()
@click.pass_contex
def update(ctx, client_uid):
    """Updates a client"""
    client_service =ClientService(ctx.obj['clients_table'])

    client_list = client_service.list_clients()

    client = [client for client in client_list if client['uid']== client_uid]

    if client:
        client = _update_client_flow(Client(**client[0]))
        client_service.update_client(client)
        
        click.echo('Client updated')
    else:
        click.echo('Client not found')


def _update_client_flow(client):
    click.echo('Leavee empty if you want to modyfy the value')

    client.name = click.prompt('new name', type=str, default=client.name)
    client.company = click.prompt('new company', type=str, default=client.company)
    client.email = click.prompt('new email', type=str, default=client.email)
    client.position = click.prompt('new position', type=str, default=client.position)

    return client 
@clients.command()
@click.pass_contex
def delete(ctx, client_uid):
    """Delete a client"""
    client_service = ClientService(ctx.obj['clients_table'])
    client_list = client_service.list_clients()
    client = [client for client in client_list if client['uid'] == client_uid]
    
    if client:
        client_service.delete_client(Client(**client[0]))

        click.echo('Client deleted')
    else:
        click.echo('Client not found')

all = clients 

