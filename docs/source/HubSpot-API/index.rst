HubSpot API
==============================================================================


Overview
------------------------------------------------------------------------------
作为开发者, 我们肯定不能满足于仅仅使用 UI 上的鼠标点击来操作 HubSpot. 我们当然希望通过程序调用来实现更高阶的自动化功能. 要实现这种更高阶的自动化功能, 就需要使用它的API.

Reference

- `HubSpot Developer Docs <https://developers.hubspot.com/docs/>`_


Private App vs Public App
------------------------------------------------------------------------------
要使用 API 就需要创建 API Key, 要创建 API Key 就要先创建 App. HubSpot 有两种 APP.

1. 一种是叫做 Private APP, Private APP 是指你自己有一个 HubSpot 账户, 然后在你的账户中创建这个APP. 它只在你的账户内生效, 是给自己使用的APP.
2. 另一种是 Public APP. 因为 HubSpot 是一个平台, 有许多第三方插件. 这些插件的作者需要创建一个 Public APP. 当用户想使用这些插件时, 他们会授权给这些第三方 APP, 从而实现各种自动化功能.

Reference:

- `Building apps overview <https://developers.hubspot.com/docs/guides/apps/overview>`_


Scope
------------------------------------------------------------------------------
创建了 API Key 之后, 这个 API Key 能操作的 Resources 列表和 Operations 就叫做 Scope. 你创建 API Key 的时候必须要选择 Scope, 创建完之后也可以改.

Reference:

- `Scope <https://developers.hubspot.com/docs/guides/apps/authentication/scopes>`_


Rate Limit
------------------------------------------------------------------------------
每个月 API 的调用次数是有限的. 根据官方文档, 一个 Starter API Plan 可以调用 250K 次每月 (也就是 8.3k) 每天. 如果你需要更多的 API Limit, 那么你需要购买 Increase API Limits, 费用大约是 $500 = 1M 次, 最多只能买 2 次 (有点扣扣搜搜)

- `Private App Limits <https://developers.hubspot.com/docs/guides/apps/private-apps/overview#private-app-limits>`_
- `API Usage guidelines <https://developers.hubspot.com/docs/guides/apps/api-usage/usage-details>`_
- `Increase API Limits <https://legal.hubspot.com/hubspot-product-and-services-catalog>`_


API Documents
------------------------------------------------------------------------------
想要查看对每一种 Resource (例如 Form, CMS) 进行 CRUD 操作的 API 文档, 可以在这个 `官方文档 <https://developers.hubspot.com/docs/reference/api/overview>`_ 中查看.
