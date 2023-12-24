# rabbit-chatter

Rabbit Chatter is a project for simulating a network of automated chat bots. It
consists of a chat server and any number of chat bots that will automatically
chat with each other. Messages will be managed with a RabbitMQ queue.

Initially, clients will

## Use cases

- Demo application for teaching container orchestrators such as Kubernetes
- Demo application for teaching infrastructure monitoring
- Learning how queues work
- Twitter simulator?
- ¯\_(ツ)\_/¯

## Deploying

The `deployment/` directory contains files for deploying a server and
several clients as local processes, Docker Compose containers, and
Kubernetes containers. Deployments for EKS, GKE are inevitable.

## Ideas

- Plug-in chat dialects. For now, chats are randomly generated
  gibberish. Why not generate the chats using ChatGPT, algorithms,
  SMS conversation exports, etc.?
- Web dashboard
  - Queue statistics
  - Client list
  - Conversation list
  - Eaves drop

## Development

For now, the easiest development environment is to run a rabbitmq container
and then run multiple processes in a virtualenvironment. For example:

```sh
docker run -d --hostname rcq --name rabbit-chatter-server rabbitmq:3
python3 -m venv rabbit-chatter
source rabbit-chatter/bin/activate
pip3 install -r requirements.txt
python3 client.py &
python3 client.py &
...
```

## Notes

Should every conversation have its own queue? For example, between client abc123
and def456, the queue could be `abc123-def456`.

This suggests each client should name itself on startup.

Each client should have a way to get a list of all other clients, and choose
a client to chat with.

Does that mean we need a directory service? Or can a client query the rabbitmq
server to get a list of queues? Would a client's queue essentially be a
public tweet? And DMs the client-client queues reprenting a DM thread?

Yes, RabbitMQ has a management interface. But clients require a username and
password to make HTTP requests to it. I might be better to have a queue-manager
process/container as a proxy to provide lists of channels to new clients.
