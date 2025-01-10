Event Webhook
==============================================================================


Overview
------------------------------------------------------------------------------
Event Webhook 是软件服务提供商提供的一种和外部系统进行通信的机制. 我们以 HubSpot 为例, 它的原理简单来说就是: 当 HubSpot 系统中发生了某些事件, 例如一个用户 Submit 了一个 Form, 那么 HubSpot 就会把这个 Event 的 metadata (通常是一个 JSON) 作为 Body 发送给一个 HTTP Endpoint. 这个 HTTP Endpoint 就是外部系统或者你自己所维护的一个系统, 这个外部系统收到这个 Event 之后就可以用程序做一些你想做的事情了.


Webhook in HubSpot Workflows
------------------------------------------------------------------------------
Webhook 在 HubSpot 中只能和 Workflows 一起使用. Workflow 顾名思义就是你可以定义一个流程, 每当从一个节点移动到另一个节点时就会产生一个 Event, 然后就可以用 Webhook 把这个 Event 发出去. HubSpot 貌似不支持 Subscribe 任何的 Event (我是这么理解的, 到底对不对我不确定).

而 Workflows 又只有在这些高级的 Plan 中 (至少 $800 一个月) 才有:

- Marketing Hub Professional, Enterprise
- Sales Hub Professional, Enterprise
- Service Hub Professional, Enterprise
- Operations Hub Professional, Enterprise

而 Webhook 只有在 Operations Hub Professional, Enterprise Plan 中才有.

所以在我看来 Webhook 不是一个实用功能, 只有企业规模达到一定程度以后才可能适用.

Reference:

- `Create workflows <https://knowledge.hubspot.com/workflows/create-workflows>`_
- `Use webhooks with HubSpot workflows <https://knowledge.hubspot.com/workflows/how-do-i-use-webhooks-with-hubspot-workflows>`_
