ì="A path prefix must not end with '/', as the routes will start with '/'"
ë="A path prefix must start with '/'"
ê='\n                Mark all *path operations* in this router as deprecated.\n\n                It will be added to the generated OpenAPI (e.g. visible at `/docs`).\n\n                Read more about it in the\n                [FastAPI docs for Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/).\n                '
é='\n                OpenAPI callbacks that should apply to all *path operations* in this\n                router.\n\n                It will be added to the generated OpenAPI (e.g. visible at `/docs`).\n\n                Read more about it in the\n                [FastAPI docs for OpenAPI Callbacks](https://fastapi.tiangolo.com/advanced/openapi-callbacks/).\n                '
è='\n                Additional responses to be shown in OpenAPI.\n\n                It will be added to the generated OpenAPI (e.g. visible at `/docs`).\n\n                Read more about it in the\n                [FastAPI docs for Additional Responses in OpenAPI](https://fastapi.tiangolo.com/advanced/additional-responses/).\n\n                And in the\n                [FastAPI docs for Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-an-apirouter-with-a-custom-prefix-tags-responses-and-dependencies).\n                '
ç='\n                The default response class to be used.\n\n                Read more in the\n                [FastAPI docs for Custom Response - HTML, Stream, File, others](https://fastapi.tiangolo.com/advanced/custom-response/#default-response-class).\n                '
æ='\n                A list of dependencies (using `Depends()`) to be applied to all the\n                *path operations* in this router.\n\n                Read more about it in the\n                [FastAPI docs for Bigger Applications - Multiple Files](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-an-apirouter-with-a-custom-prefix-tags-responses-and-dependencies).\n                '
å='\n                A list of tags to be applied to all the *path operations* in this\n                router.\n\n                It will be added to the generated OpenAPI (e.g. visible at `/docs`).\n\n                Read more about it in the\n                [FastAPI docs for Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/).\n                '
ä='An optional path prefix for the router.'
ã='function'
â='fastapi_inner_astack not found in request scope'
á='fastapi_function_astack'
Ø='dependant.call must be a function'
Ö=getattr
Ï='fastapi_inner_astack'
Í=list
Ë='\n                Extra metadata to be included in the OpenAPI schema for this *path\n                operation*.\n\n                Read more about it in the\n                [FastAPI docs for Path Operation Advanced Configuration](https://fastapi.tiangolo.com/advanced/path-operation-advanced-configuration/#custom-openapi-path-operation-schema).\n                '
É="\n                List of *path operations* that will be used as OpenAPI callbacks.\n\n                This is only for OpenAPI documentation, the callbacks won't be used\n                directly.\n\n                It will be added to the generated OpenAPI (e.g. visible at `/docs`).\n\n                Read more about it in the\n                [FastAPI docs for OpenAPI Callbacks](https://fastapi.tiangolo.com/advanced/openapi-callbacks/).\n                "
È='\n                Name for this *path operation*. Only used internally.\n                '
Ç='\n                Response class to be used for this *path operation*.\n\n                This will not be used if you return a response directly.\n\n                Read more about it in the\n                [FastAPI docs for Custom Response - HTML, Stream, File, others](https://fastapi.tiangolo.com/advanced/custom-response/#redirectresponse).\n                '
Å='\n                Include this *path operation* in the generated OpenAPI schema.\n\n                This affects the generated OpenAPI (e.g. visible at `/docs`).\n\n                Read more about it in the\n                [FastAPI docs for Query Parameters and String Validations](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#exclude-parameters-from-openapi).\n                '
Ä='\n                Configuration passed to Pydantic to define if the response data should\n                exclude fields set to `None`.\n\n                This is much simpler (less smart) than `response_model_exclude_unset`\n                and `response_model_exclude_defaults`. You probably want to use one of\n                those two instead of this one, as those allow returning `None` values\n                when it makes sense.\n\n                Read more about it in the\n                [FastAPI docs for Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/#response_model_exclude_none).\n                '
Ã='\n                Configuration passed to Pydantic to define if the response data\n                should have all the fields, including the ones that have the same value\n                as the default. This is different from `response_model_exclude_unset`\n                in that if the fields are set but contain the same default values,\n                they will be excluded from the response.\n\n                When `True`, default values are omitted from the response.\n\n                Read more about it in the\n                [FastAPI docs for Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/#use-the-response_model_exclude_unset-parameter).\n                '
Â='\n                Configuration passed to Pydantic to define if the response data\n                should have all the fields, including the ones that were not set and\n                have their default values. This is different from\n                `response_model_exclude_defaults` in that if the fields are set,\n                they will be included in the response, even if the value is the same\n                as the default.\n\n                When `True`, default values are omitted from the response.\n\n                Read more about it in the\n                [FastAPI docs for Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/#use-the-response_model_exclude_unset-parameter).\n                '
Á='\n                Configuration passed to Pydantic to define if the response model\n                should be serialized by alias when an alias is used.\n\n                Read more about it in the\n                [FastAPI docs for Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/#response_model_include-and-response_model_exclude).\n                '
À='\n                Configuration passed to Pydantic to exclude certain fields in the\n                response data.\n\n                Read more about it in the\n                [FastAPI docs for Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/#response_model_include-and-response_model_exclude).\n                '
º='\n                Configuration passed to Pydantic to include only certain fields in the\n                response data.\n\n                Read more about it in the\n                [FastAPI docs for Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/#response_model_include-and-response_model_exclude).\n                '
µ='\n                Custom operation ID to be used by this *path operation*.\n\n                By default, it is generated automatically.\n\n                If you provide a custom operation ID, you need to make sure it is\n                unique for the whole API.\n\n                You can customize the\n                operation ID generation with the parameter\n                `generate_unique_id_function` in the `FastAPI` class.\n\n                Read more about it in the\n                [FastAPI docs about how to Generate Clients](https://fastapi.tiangolo.com/advanced/generate-clients/#custom-generate-unique-id-function).\n                '
ª='\n                Mark this *path operation* as deprecated.\n\n                It will be added to the generated OpenAPI (e.g. visible at `/docs`).\n                '
z='\n                Additional responses that could be returned by this *path operation*.\n\n                It will be added to the generated OpenAPI (e.g. visible at `/docs`).\n                '
y='\n                The description for the default response.\n\n                It will be added to the generated OpenAPI (e.g. visible at `/docs`).\n                '
w='\n                A description for the *path operation*.\n\n                If not provided, it will be extracted automatically from the docstring\n                of the *path operation function*.\n\n                It can contain Markdown.\n\n                It will be added to the generated OpenAPI (e.g. visible at `/docs`).\n\n                Read more about it in the\n                [FastAPI docs for Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/).\n                '
v='\n                A summary for the *path operation*.\n\n                It will be added to the generated OpenAPI (e.g. visible at `/docs`).\n\n                Read more about it in the\n                [FastAPI docs for Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/).\n                '
u='\n                A list of dependencies (using `Depends()`) to be applied to the\n                *path operation*.\n\n                Read more about it in the\n                [FastAPI docs for Dependencies in path operation decorators](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/).\n                '
t='\n                A list of tags to be applied to the *path operation*.\n\n                It will be added to the generated OpenAPI (e.g. visible at `/docs`).\n\n                Read more about it in the\n                [FastAPI docs for Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/#tags).\n                '
s='\n                The default status code to be used for the response.\n\n                You could override the status code by returning a response directly.\n\n                Read more about it in the\n                [FastAPI docs for Response Status Code](https://fastapi.tiangolo.com/tutorial/response-status-code/).\n                '
r="\n                The type to use for the response.\n\n                It could be any valid Pydantic *field* type. So, it doesn't have to\n                be a Pydantic model, it could be other things, like a `list`, `dict`,\n                etc.\n\n                It will be used for:\n\n                * Documentation: the generated OpenAPI (and the UI at `/docs`) will\n                    show it as the response (JSON Schema).\n                * Serialization: you could return an arbitrary object and the\n                    `response_model` would be used to serialize that object into the\n                    corresponding JSON.\n                * Filtering: the JSON sent to the client will only contain the data\n                    (fields) defined in the `response_model`. If you returned an object\n                    that contains an attribute `password` but the `response_model` does\n                    not include that field, the JSON sent to the client would not have\n                    that `password`.\n                * Validation: whatever you return will be serialized with the\n                    `response_model`, converting any data as necessary to generate the\n                    corresponding JSON. But if the data in the object returned is not\n                    valid, that would mean a violation of the contract with the client,\n                    so it's an error from the API developer. So, FastAPI will raise an\n                    error and return a 500 error code (Internal Server Error).\n\n                Read more about it in the\n                [FastAPI docs for Response Model](https://fastapi.tiangolo.com/tutorial/response-model/).\n                "
q='\n                The URL path to be used for this *path operation*.\n\n                For example, in `http://example.com/items`, the path is `/items`.\n                '
o='\n                Customize the function used to generate unique IDs for the *path\n                operations* shown in the generated OpenAPI.\n\n                This is particularly useful when automatically generating clients or\n                SDKs for your API.\n\n                Read more about it in the\n                [FastAPI docs about how to Generate Clients](https://fastapi.tiangolo.com/advanced/generate-clients/#custom-generate-unique-id-function).\n                '
n='Successful Response'
g=isinstance
f=int
d=True
X=False
V=bool
T=str
A=None
import dataclasses as Ù,email.message,functools as í,inspect,json
from contextlib import AsyncExitStack as Ì,asynccontextmanager as î
from enum import Enum as k,IntEnum
from typing import Any as W,Awaitable as Ð,Callable as a,Collection as ð,Dict as Z,List as c,Optional as S,Sequence as h,Set,Type as j,Union as b
from annotated_doc import Doc as Q
from D import params as i,temp_pydantic_v1_params as ñ
from D.B import ă,Ă,ā,Ā,ÿ,Ą
from D.G import F,J
from D.H.A import Č
from D.H.B import ĉ,ċ,Ć,ą,Ĉ,Ċ,ć
from D.I import L
from D.K import ý,û,þ,ü
from D.Y import P,x
from D.Z import N,K,D,O,I
from pydantic import BaseModel as ò
from F import routing as Î
from F.A import Ý
from F.B import G
from F.F import Æ
from F.K import Ú
from F.N import Y
from F.O import H,C
from F.P import U,M,e,p
from F.V import E,Ê,B,Ò,Ñ,Send
from F.W import Û
from typing_extensions import Annotated as R,deprecated as Þ
from asyncio import iscoroutinefunction as ß
def ó(func:a[[Y],b[Ð[C],C]]):
	'\n    Takes a function or coroutine `func(request) -> response`,\n    and returns an ASGI application.\n    ';A=func;D=A if G(A)else í.partial(Æ,A)
	async def B(scope:Ñ,receive:Ò,send:Send):
		B=receive;A=scope;C=Y(A,B,send)
		async def E(scope:Ñ,receive:Ò,send:Send):
			A=scope;B=X
			async with Ì()as E:
				A[Ï]=E
				async with Ì()as F:A[á]=F;G=await D(C)
				await G(A,receive,send);B=d
			if not B:raise ý("Response not awaited. There's a high chance that the application code is raising an exception and a dependency with yield has a block with a bare except, or a block with except Exception, and is not raising the exception again. Read more about it in the docs: https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#dependencies-with-yield-and-except")
		await Ý(E,C)(A,B,send)
	return B
def ô(func:a[[Û],Ð[A]]):
	'\n    Takes a coroutine `func(session)`, and returns an ASGI application.\n    '
	async def A(scope:Ñ,receive:Ò,send:Send):
		B=receive;A=scope;C=Û(A,receive=B,send=send)
		async def D(scope:Ñ,receive:Ò,send:Send):
			A=scope
			async with Ì()as B:
				A[Ï]=B
				async with Ì()as D:A[á]=D;await func(C)
		await Ý(D,C)(A,B,send)
	return A
def Ô(res:W,*,exclude_unset:V,exclude_defaults:V=X,exclude_none:V=X):
	E=exclude_none;D=exclude_defaults;C=exclude_unset;B=res
	if g(B,ò):
		F=Ö(ā(B),'read_with_orm_mode',A)
		if F:return B
		return Ā(B,by_alias=d,exclude_unset=C,exclude_defaults=D,exclude_none=E)
	elif g(B,Í):return[Ô(A,exclude_unset=C,exclude_defaults=D,exclude_none=E)for A in B]
	elif g(B,dict):return{A:Ô(B,exclude_unset=C,exclude_defaults=D,exclude_none=E)for(A,B)in B.items()}
	elif Ù.is_dataclass(B):assert not g(B,type);return Ù.asdict(B)
	return B
def õ(original_context:B[W],nested_context:B[W]):
	@î
	async def B(app:E):
		async with original_context(app)as B:
			async with nested_context(app)as C:
				if C is A and B is A:yield A
				else:yield{**(C or{}),**(B or{})}
	return B
async def ö(*,field:S[ă]=A,response_content:W,include:S[x]=A,exclude:S[x]=A,by_alias:V=d,exclude_unset:V=X,exclude_defaults:V=X,exclude_none:V=X,is_coroutine:V=d):
	N='response';M='serialize';K=by_alias;J=exclude;I=include;G=exclude_none;F=exclude_defaults;E=exclude_unset;B=response_content;A=field
	if A:
		D=[]
		if not hasattr(A,M):B=Ô(B,exclude_unset=E,exclude_defaults=F,exclude_none=G)
		if is_coroutine:H,C=A.validate(B,{},loc=(N,))
		else:H,C=await Æ(A.validate,B,{},loc=(N,))
		if g(C,Í):D.extend(C)
		elif C:D.append(C)
		if D:raise þ(errors=ÿ(D),body=B)
		if hasattr(A,M):return A.serialize(H,include=I,exclude=J,by_alias=K,exclude_unset=E,exclude_defaults=F,exclude_none=G)
		return L(H,include=I,exclude=J,by_alias=K,exclude_unset=E,exclude_defaults=F,exclude_none=G)
	else:return L(B)
async def ø(*,dependant:Č,values:Z[T,W],is_coroutine:V):
	C=values;B=dependant;assert B.call is not A,Ø
	if is_coroutine:return await B.call(**C)
	else:return await Æ(B.call,**C)
def ù(dependant:Č,body_field:S[ă]=A,status_code:S[f]=A,response_class:b[j[C],J]=F(H),response_field:S[ă]=A,response_model_include:S[x]=A,response_model_exclude:S[x]=A,response_model_by_alias:V=d,response_model_exclude_unset:V=X,response_model_exclude_defaults:V=X,response_model_exclude_none:V=X,dependency_overrides_provider:S[W]=A,embed_body_fields:V=X):
	Q=status_code;B=response_class;M=body_field;K=dependant;assert K.call is not A,Ø;R=ß(K.call);h=M and g(M.field_info,(i.Form,ñ.Form))
	if g(B,J):S=B.value
	else:S=B
	async def D(request:Y):
		f='status_code';e='content-type';B=request;E=A;U=B.scope.get('fastapi_middleware_astack');assert g(U,Ì),'fastapi_middleware_astack not found in request scope'
		try:
			F=A
			if M:
				if h:F=await B.form();U.push_async_callback(F.close)
				else:
					V=await B.body()
					if V:
						J=Ă;X=B.headers.get(e)
						if not X:J=await B.json()
						else:
							N=email.message.Message();N[e]=X
							if N.get_content_maintype()=='application':
								Y=N.get_content_subtype()
								if Y=='json'or Y.endswith('+json'):J=await B.json()
						if J!=Ă:F=J
						else:F=V
		except json.JSONDecodeError as G:O=û([{'type':'json_invalid','loc':('body',G.pos),'msg':'JSON decode error','input':{},'ctx':{'error':G.msg}}],body=G.doc);raise O from G
		except Ú:raise
		except Exception as G:i=Ú(status_code=400,detail='There was an error parsing the body');raise i from G
		L=[];a=B.scope.get(Ï);assert g(a,Ì),â;D=await ć(request=B,dependant=K,body=F,dependency_overrides_provider=dependency_overrides_provider,async_exit_stack=a,embed_body_fields=embed_body_fields);L=D.errors
		if not L:
			H=await ø(dependant=K,values=D.values,is_coroutine=R)
			if g(H,C):
				if H.background is A:H.background=D.background_tasks
				E=H
			else:
				P={'background':D.background_tasks};d=Q if Q else D.response.status_code
				if d is not A:P[f]=d
				if D.response.status_code:P[f]=D.response.status_code
				j=await ö(field=response_field,response_content=H,include=response_model_include,exclude=response_model_exclude,by_alias=response_model_by_alias,exclude_unset=response_model_exclude_unset,exclude_defaults=response_model_exclude_defaults,exclude_none=response_model_exclude_none,is_coroutine=R);E=S(j,**P)
				if not I(E.status_code):E.body=b''
				E.headers.raw.extend(D.response.headers.raw)
		if L:O=û(ÿ(L),body=F);raise O
		assert E;return E
	return D
def ú(dependant:Č,dependency_overrides_provider:S[W]=A,embed_body_fields:V=X):
	B=dependant
	async def C(websocket:Û):
		D=websocket;E=D.scope.get(Ï);assert g(E,Ì),â;C=await ć(request=D,dependant=B,dependency_overrides_provider=dependency_overrides_provider,async_exit_stack=E,embed_body_fields=embed_body_fields)
		if C.errors:raise ü(ÿ(C.errors))
		assert B.call is not A,Ø;await B.call(**C.values)
	return C
class à(Î.WebSocketRoute):
	def __init__(B,path:T,endpoint:a[...,W],*,name:S[T]=A,dependencies:S[h[i.Depends]]=A,dependency_overrides_provider:S[W]=A):
		C=endpoint;B.path=path;B.endpoint=C;B.name=p(C)if name is A else name;B.dependencies=Í(dependencies or[]);B.path_regex,B.path_format,B.param_convertors=e(path);B.dependant=Ć(path=B.path_format,call=B.endpoint,scope=ã)
		for D in B.dependencies[::-1]:B.dependant.dependencies.insert(0,Ĉ(depends=D,path=B.path_format))
		B._flat_dependant=ą(B.dependant);B._embed_body_fields=ĉ(B._flat_dependant.body_params);B.app=ô(ú(dependant=B.dependant,dependency_overrides_provider=dependency_overrides_provider,embed_body_fields=B._embed_body_fields))
	def matches(C,scope:Ñ):
		A,B=super().matches(scope)
		if A!=M.NONE:B['route']=C
		return A,B
class m(Î.Route):
	def __init__(B,path:T,endpoint:a[...,W],*,response_model:W=F(A),status_code:S[f]=A,tags:S[c[b[T,k]]]=A,dependencies:S[h[i.Depends]]=A,summary:S[T]=A,description:S[T]=A,response_description:T=n,responses:S[Z[b[f,T],Z[T,W]]]=A,deprecated:S[V]=A,name:S[T]=A,methods:S[b[Set[T],c[T]]]=A,operation_id:S[T]=A,response_model_include:S[x]=A,response_model_exclude:S[x]=A,response_model_by_alias:V=d,response_model_exclude_unset:V=X,response_model_exclude_defaults:V=X,response_model_exclude_none:V=X,include_in_schema:V=d,response_class:b[j[C],J]=F(H),dependency_overrides_provider:S[W]=A,callbacks:S[c[U]]=A,openapi_extra:S[Z[T,W]]=A,generate_unique_id_function:b[a[['APIRoute'],T],J]=F(D)):
		V='serialization';L=methods;G=generate_unique_id_function;F=response_model;E=endpoint;D=status_code;B.path=path;B.endpoint=E
		if g(F,J):
			P=Ċ(E)
			if Ą(P,C):F=A
			else:F=P
		B.response_model=F;B.summary=summary;B.response_description=response_description;B.deprecated=deprecated;B.operation_id=operation_id;B.response_model_include=response_model_include;B.response_model_exclude=response_model_exclude;B.response_model_by_alias=response_model_by_alias;B.response_model_exclude_unset=response_model_exclude_unset;B.response_model_exclude_defaults=response_model_exclude_defaults;B.response_model_exclude_none=response_model_exclude_none;B.include_in_schema=include_in_schema;B.response_class=response_class;B.dependency_overrides_provider=dependency_overrides_provider;B.callbacks=callbacks;B.openapi_extra=openapi_extra;B.generate_unique_id_function=G;B.tags=tags or[];B.responses=responses or{};B.name=p(E)if name is A else name;B.path_regex,B.path_format,B.param_convertors=e(path)
		if L is A:L=['GET']
		B.methods={method.upper()for method in L}
		if g(G,J):Q=G.value
		else:Q=G
		B.unique_id=B.operation_id or Q(B)
		if g(D,IntEnum):D=f(D)
		B.status_code=D
		if B.response_model:assert I(D),f"Status code {D} must not have a response body";M='Response_'+B.unique_id;B.response_field=K(name=M,type_=B.response_model,mode=V);B.secure_cloned_response_field=N(B.response_field)
		else:B.response_field=A;B.secure_cloned_response_field=A
		B.dependencies=Í(dependencies or[]);B.description=description or inspect.cleandoc(B.endpoint.__doc__ or'');B.description=B.description.split('\x0c')[0].strip();O={}
		for(H,R)in B.responses.items():
			assert g(R,dict),'An additional response must be a dict';U=R.get('model')
			if U:assert I(H),f"Status code {H} must not have a response body";M=f"Response_{H}_{B.unique_id}";W=K(name=M,type_=U,mode=V);O[H]=W
		if O:B.response_fields=O
		else:B.response_fields={}
		assert callable(E),'An endpoint must be a callable';B.dependant=Ć(path=B.path_format,call=B.endpoint,scope=ã)
		for X in B.dependencies[::-1]:B.dependant.dependencies.insert(0,Ĉ(depends=X,path=B.path_format))
		B._flat_dependant=ą(B.dependant);B._embed_body_fields=ĉ(B._flat_dependant.body_params);B.body_field=ċ(flat_dependant=B._flat_dependant,name=B.unique_id,embed_body_fields=B._embed_body_fields);B.app=ó(B.get_route_handler())
	def get_route_handler(A):return ù(dependant=A.dependant,body_field=A.body_field,status_code=A.status_code,response_class=A.response_class,response_field=A.secure_cloned_response_field,response_model_include=A.response_model_include,response_model_exclude=A.response_model_exclude,response_model_by_alias=A.response_model_by_alias,response_model_exclude_unset=A.response_model_exclude_unset,response_model_exclude_defaults=A.response_model_exclude_defaults,response_model_exclude_none=A.response_model_exclude_none,dependency_overrides_provider=A.dependency_overrides_provider,embed_body_fields=A._embed_body_fields)
	def matches(C,scope:Ñ):
		A,B=super().matches(scope)
		if A!=M.NONE:B['route']=C
		return A,B
class Õ(Î.Router):
	'\n    `APIRouter` class, used to group *path operations*, for example to structure\n    an app in multiple files. It would then be included in the `FastAPI` app, or\n    in another `APIRouter` (ultimately included in the app).\n\n    Read more about it in the\n    [FastAPI docs for Bigger Applications - Multiple Files](https://fastapi.tiangolo.com/tutorial/bigger-applications/).\n\n    ## Example\n\n    ```python\n    from fastapi import APIRouter, FastAPI\n\n    app = FastAPI()\n    router = APIRouter()\n\n\n    @router.get("/users/", tags=["users"])\n    async def read_users():\n        return [{"username": "Rick"}, {"username": "Morty"}]\n\n\n    app.include_router(router)\n    ```\n    '
	def __init__(A,*,prefix:R[T,Q(ä)]='',tags:R[S[c[b[T,k]]],Q(å)]=A,dependencies:R[S[h[i.Depends]],Q(æ)]=A,default_response_class:R[j[C],Q(ç)]=F(H),responses:R[S[Z[b[f,T],Z[T,W]]],Q(è)]=A,callbacks:R[S[c[U]],Q(é)]=A,routes:R[S[c[U]],Q("\n                **Note**: you probably shouldn't use this parameter, it is inherited\n                from Starlette and supported for compatibility.\n\n                ---\n\n                A list of routes to serve incoming HTTP and WebSocket requests.\n                "),Þ("\n                You normally wouldn't use this parameter with FastAPI, it is inherited\n                from Starlette and supported for compatibility.\n\n                In FastAPI, you normally would use the *path operation methods*,\n                like `router.get()`, `router.post()`, etc.\n                ")]=A,redirect_slashes:R[V,Q("\n                Whether to detect and redirect slashes in URLs when the client doesn't\n                use the same format.\n                ")]=d,default:R[S[Ê],Q('\n                Default function handler for this router. Used to handle\n                404 Not Found errors.\n                ')]=A,dependency_overrides_provider:R[S[W],Q("\n                Only used internally by FastAPI to handle dependency overrides.\n\n                You shouldn't need to use it. It normally points to the `FastAPI` app\n                object.\n                ")]=A,route_class:R[j[m],Q('\n                Custom route (*path operation*) class to be used by this router.\n\n                Read more about it in the\n                [FastAPI docs for Custom Request and APIRoute class](https://fastapi.tiangolo.com/how-to/custom-request-and-route/#custom-apiroute-class-in-a-router).\n                ')]=m,on_startup:R[S[h[a[[],W]]],Q('\n                A list of startup event handler functions.\n\n                You should instead use the `lifespan` handlers.\n\n                Read more in the [FastAPI docs for `lifespan`](https://fastapi.tiangolo.com/advanced/events/).\n                ')]=A,on_shutdown:R[S[h[a[[],W]]],Q('\n                A list of shutdown event handler functions.\n\n                You should instead use the `lifespan` handlers.\n\n                Read more in the\n                [FastAPI docs for `lifespan`](https://fastapi.tiangolo.com/advanced/events/).\n                ')]=A,lifespan:R[S[B[W]],Q('\n                A `Lifespan` context manager handler. This replaces `startup` and\n                `shutdown` functions with a single context manager.\n\n                Read more in the\n                [FastAPI docs for `lifespan`](https://fastapi.tiangolo.com/advanced/events/).\n                ')]=A,deprecated:R[S[V],Q(ê)]=A,include_in_schema:R[V,Q('\n                To include (or not) all the *path operations* in this router in the\n                generated OpenAPI.\n\n                This affects the generated OpenAPI (e.g. visible at `/docs`).\n\n                Read more about it in the\n                [FastAPI docs for Query Parameters and String Validations](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#exclude-parameters-from-openapi).\n                ')]=d,generate_unique_id_function:R[a[[m],T],Q(o)]=F(D)):
		B=prefix;super().__init__(routes=routes,redirect_slashes=redirect_slashes,default=default,on_startup=on_startup,on_shutdown=on_shutdown,lifespan=lifespan)
		if B:assert B.startswith('/'),ë;assert not B.endswith('/'),ì
		A.prefix=B;A.tags=tags or[];A.dependencies=Í(dependencies or[]);A.deprecated=deprecated;A.include_in_schema=include_in_schema;A.responses=responses or{};A.callbacks=callbacks or[];A.dependency_overrides_provider=dependency_overrides_provider;A.route_class=route_class;A.default_response_class=default_response_class;A.generate_unique_id_function=generate_unique_id_function
	def route(A,path:T,methods:S[ð[T]]=A,name:S[T]=A,include_in_schema:V=d):
		def B(func:P):A.add_route(path,func,methods=methods,name=name,include_in_schema=include_in_schema);return func
		return B
	def add_api_route(A,path:T,endpoint:a[...,W],*,response_model:W=F(A),status_code:S[f]=A,tags:S[c[b[T,k]]]=A,dependencies:S[h[i.Depends]]=A,summary:S[T]=A,description:S[T]=A,response_description:T=n,responses:S[Z[b[f,T],Z[T,W]]]=A,deprecated:S[V]=A,methods:S[b[Set[T],c[T]]]=A,operation_id:S[T]=A,response_model_include:S[x]=A,response_model_exclude:S[x]=A,response_model_by_alias:V=d,response_model_exclude_unset:V=X,response_model_exclude_defaults:V=X,response_model_exclude_none:V=X,include_in_schema:V=d,response_class:b[j[C],J]=F(H),name:S[T]=A,route_class_override:S[j[m]]=A,callbacks:S[c[U]]=A,openapi_extra:S[Z[T,W]]=A,generate_unique_id_function:b[a[[m],T],J]=F(D)):
		D=callbacks;C=dependencies;B=responses;H=route_class_override or A.route_class;B=B or{};I={**A.responses,**B};J=O(response_class,A.default_response_class);E=A.tags.copy()
		if tags:E.extend(tags)
		F=A.dependencies.copy()
		if C:F.extend(C)
		G=A.callbacks.copy()
		if D:G.extend(D)
		K=O(generate_unique_id_function,A.generate_unique_id_function);L=H(A.prefix+path,endpoint=endpoint,response_model=response_model,status_code=status_code,tags=E,dependencies=F,summary=summary,description=description,response_description=response_description,responses=I,deprecated=deprecated or A.deprecated,methods=methods,operation_id=operation_id,response_model_include=response_model_include,response_model_exclude=response_model_exclude,response_model_by_alias=response_model_by_alias,response_model_exclude_unset=response_model_exclude_unset,response_model_exclude_defaults=response_model_exclude_defaults,response_model_exclude_none=response_model_exclude_none,include_in_schema=include_in_schema and A.include_in_schema,response_class=J,name=name,dependency_overrides_provider=A.dependency_overrides_provider,callbacks=G,openapi_extra=openapi_extra,generate_unique_id_function=K);A.routes.append(L)
	def api_route(A,path:T,*,response_model:W=F(A),status_code:S[f]=A,tags:S[c[b[T,k]]]=A,dependencies:S[h[i.Depends]]=A,summary:S[T]=A,description:S[T]=A,response_description:T=n,responses:S[Z[b[f,T],Z[T,W]]]=A,deprecated:S[V]=A,methods:S[c[T]]=A,operation_id:S[T]=A,response_model_include:S[x]=A,response_model_exclude:S[x]=A,response_model_by_alias:V=d,response_model_exclude_unset:V=X,response_model_exclude_defaults:V=X,response_model_exclude_none:V=X,include_in_schema:V=d,response_class:j[C]=F(H),name:S[T]=A,callbacks:S[c[U]]=A,openapi_extra:S[Z[T,W]]=A,generate_unique_id_function:a[[m],T]=F(D)):
		def B(func:P):A.add_api_route(path,func,response_model=response_model,status_code=status_code,tags=tags,dependencies=dependencies,summary=summary,description=description,response_description=response_description,responses=responses,deprecated=deprecated,methods=methods,operation_id=operation_id,response_model_include=response_model_include,response_model_exclude=response_model_exclude,response_model_by_alias=response_model_by_alias,response_model_exclude_unset=response_model_exclude_unset,response_model_exclude_defaults=response_model_exclude_defaults,response_model_exclude_none=response_model_exclude_none,include_in_schema=include_in_schema,response_class=response_class,name=name,callbacks=callbacks,openapi_extra=openapi_extra,generate_unique_id_function=generate_unique_id_function);return func
		return B
	def add_api_websocket_route(A,path:T,endpoint:a[...,W],name:S[T]=A,*,dependencies:S[h[i.Depends]]=A):
		B=dependencies;C=A.dependencies.copy()
		if B:C.extend(B)
		D=à(A.prefix+path,endpoint=endpoint,name=name,dependencies=C,dependency_overrides_provider=A.dependency_overrides_provider);A.routes.append(D)
	def websocket(A,path:R[T,Q('\n                WebSocket path.\n                ')],name:R[S[T],Q('\n                A name for the WebSocket. Only used internally.\n                ')]=A,*,dependencies:R[S[h[i.Depends]],Q('\n                A list of dependencies (using `Depends()`) to be used for this\n                WebSocket.\n\n                Read more about it in the\n                [FastAPI docs for WebSockets](https://fastapi.tiangolo.com/advanced/websockets/).\n                ')]=A):
		'\n        Decorate a WebSocket function.\n\n        Read more about it in the\n        [FastAPI docs for WebSockets](https://fastapi.tiangolo.com/advanced/websockets/).\n\n        **Example**\n\n        ## Example\n\n        ```python\n        from fastapi import APIRouter, FastAPI, WebSocket\n\n        app = FastAPI()\n        router = APIRouter()\n\n        @router.websocket("/ws")\n        async def websocket_endpoint(websocket: WebSocket):\n            await websocket.accept()\n            while True:\n                data = await websocket.receive_text()\n                await websocket.send_text(f"Message text was: {data}")\n\n        app.include_router(router)\n        ```\n        '
		def B(func:P):A.add_api_websocket_route(path,func,name=name,dependencies=dependencies);return func
		return B
	def websocket_route(A,path:T,name:b[T,A]=A):
		def B(func:P):A.add_websocket_route(path,func,name=name);return func
		return B
	def include_router(C,router:R['APIRouter',Q('The `APIRouter` to include.')],*,prefix:R[T,Q(ä)]='',tags:R[S[c[b[T,k]]],Q(å)]=A,dependencies:R[S[h[i.Depends]],Q(æ)]=A,default_response_class:R[j[C],Q(ç)]=F(H),responses:R[S[Z[b[f,T],Z[T,W]]],Q(è)]=A,callbacks:R[S[c[U]],Q(é)]=A,deprecated:R[S[V],Q(ê)]=A,include_in_schema:R[V,Q('\n                Include (or not) all the *path operations* in this router in the\n                generated OpenAPI schema.\n\n                This affects the generated OpenAPI (e.g. visible at `/docs`).\n                ')]=d,generate_unique_id_function:R[a[[m],T],Q(o)]=F(D)):
		'\n        Include another `APIRouter` in the same current `APIRouter`.\n\n        Read more about it in the\n        [FastAPI docs for Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/).\n\n        ## Example\n\n        ```python\n        from fastapi import APIRouter, FastAPI\n\n        app = FastAPI()\n        internal_router = APIRouter()\n        users_router = APIRouter()\n\n        @users_router.get("/users/")\n        def read_users():\n            return [{"name": "Rick"}, {"name": "Morty"}]\n\n        internal_router.include_router(users_router)\n        app.include_router(internal_router)\n        ```\n        ';L=callbacks;H=responses;G=dependencies;E=prefix;D=router
		if E:assert E.startswith('/'),ë;assert not E.endswith('/'),ì
		else:
			for M in D.routes:
				N=Ö(M,'path');P=Ö(M,'name','unknown')
				if N is not A and not N:raise ý(f"Prefix and path cannot be both empty (path operation: {P})")
		if H is A:H={}
		for B in D.routes:
			if g(B,m):
				Q={**H,**B.responses};R=O(B.response_class,D.default_response_class,default_response_class,C.default_response_class);I=[]
				if tags:I.extend(tags)
				if B.tags:I.extend(B.tags)
				F=[]
				if G:F.extend(G)
				if B.dependencies:F.extend(B.dependencies)
				J=[]
				if L:J.extend(L)
				if B.callbacks:J.extend(B.callbacks)
				S=O(B.generate_unique_id_function,D.generate_unique_id_function,generate_unique_id_function,C.generate_unique_id_function);C.add_api_route(E+B.path,B.endpoint,response_model=B.response_model,status_code=B.status_code,tags=I,dependencies=F,summary=B.summary,description=B.description,response_description=B.response_description,responses=Q,deprecated=B.deprecated or deprecated or C.deprecated,methods=B.methods,operation_id=B.operation_id,response_model_include=B.response_model_include,response_model_exclude=B.response_model_exclude,response_model_by_alias=B.response_model_by_alias,response_model_exclude_unset=B.response_model_exclude_unset,response_model_exclude_defaults=B.response_model_exclude_defaults,response_model_exclude_none=B.response_model_exclude_none,include_in_schema=B.include_in_schema and C.include_in_schema and include_in_schema,response_class=R,name=B.name,route_class_override=type(B),callbacks=J,openapi_extra=B.openapi_extra,generate_unique_id_function=S)
			elif g(B,Î.Route):T=Í(B.methods or[]);C.add_route(E+B.path,B.endpoint,methods=T,include_in_schema=B.include_in_schema,name=B.name)
			elif g(B,à):
				F=[]
				if G:F.extend(G)
				if B.dependencies:F.extend(B.dependencies)
				C.add_api_websocket_route(E+B.path,B.endpoint,dependencies=F,name=B.name)
			elif g(B,Î.WebSocketRoute):C.add_websocket_route(E+B.path,B.endpoint,name=B.name)
		for K in D.on_startup:C.add_event_handler('startup',K)
		for K in D.on_shutdown:C.add_event_handler('shutdown',K)
		C.lifespan_context=õ(C.lifespan_context,D.lifespan_context)
	def get(A,path:R[T,Q(q)],*,response_model:R[W,Q(r)]=F(A),status_code:R[S[f],Q(s)]=A,tags:R[S[c[b[T,k]]],Q(t)]=A,dependencies:R[S[h[i.Depends]],Q(u)]=A,summary:R[S[T],Q(v)]=A,description:R[S[T],Q(w)]=A,response_description:R[T,Q(y)]=n,responses:R[S[Z[b[f,T],Z[T,W]]],Q(z)]=A,deprecated:R[S[V],Q(ª)]=A,operation_id:R[S[T],Q(µ)]=A,response_model_include:R[S[x],Q(º)]=A,response_model_exclude:R[S[x],Q(À)]=A,response_model_by_alias:R[V,Q(Á)]=d,response_model_exclude_unset:R[V,Q(Â)]=X,response_model_exclude_defaults:R[V,Q(Ã)]=X,response_model_exclude_none:R[V,Q(Ä)]=X,include_in_schema:R[V,Q(Å)]=d,response_class:R[j[C],Q(Ç)]=F(H),name:R[S[T],Q(È)]=A,callbacks:R[S[c[U]],Q(É)]=A,openapi_extra:R[S[Z[T,W]],Q(Ë)]=A,generate_unique_id_function:R[a[[m],T],Q(o)]=F(D)):'\n        Add a *path operation* using an HTTP GET operation.\n\n        ## Example\n\n        ```python\n        from fastapi import APIRouter, FastAPI\n\n        app = FastAPI()\n        router = APIRouter()\n\n        @router.get("/items/")\n        def read_items():\n            return [{"name": "Empanada"}, {"name": "Arepa"}]\n\n        app.include_router(router)\n        ```\n        ';return A.api_route(path=path,response_model=response_model,status_code=status_code,tags=tags,dependencies=dependencies,summary=summary,description=description,response_description=response_description,responses=responses,deprecated=deprecated,methods=['GET'],operation_id=operation_id,response_model_include=response_model_include,response_model_exclude=response_model_exclude,response_model_by_alias=response_model_by_alias,response_model_exclude_unset=response_model_exclude_unset,response_model_exclude_defaults=response_model_exclude_defaults,response_model_exclude_none=response_model_exclude_none,include_in_schema=include_in_schema,response_class=response_class,name=name,callbacks=callbacks,openapi_extra=openapi_extra,generate_unique_id_function=generate_unique_id_function)
	def put(A,path:R[T,Q(q)],*,response_model:R[W,Q(r)]=F(A),status_code:R[S[f],Q(s)]=A,tags:R[S[c[b[T,k]]],Q(t)]=A,dependencies:R[S[h[i.Depends]],Q(u)]=A,summary:R[S[T],Q(v)]=A,description:R[S[T],Q(w)]=A,response_description:R[T,Q(y)]=n,responses:R[S[Z[b[f,T],Z[T,W]]],Q(z)]=A,deprecated:R[S[V],Q(ª)]=A,operation_id:R[S[T],Q(µ)]=A,response_model_include:R[S[x],Q(º)]=A,response_model_exclude:R[S[x],Q(À)]=A,response_model_by_alias:R[V,Q(Á)]=d,response_model_exclude_unset:R[V,Q(Â)]=X,response_model_exclude_defaults:R[V,Q(Ã)]=X,response_model_exclude_none:R[V,Q(Ä)]=X,include_in_schema:R[V,Q(Å)]=d,response_class:R[j[C],Q(Ç)]=F(H),name:R[S[T],Q(È)]=A,callbacks:R[S[c[U]],Q(É)]=A,openapi_extra:R[S[Z[T,W]],Q(Ë)]=A,generate_unique_id_function:R[a[[m],T],Q(o)]=F(D)):'\n        Add a *path operation* using an HTTP PUT operation.\n\n        ## Example\n\n        ```python\n        from fastapi import APIRouter, FastAPI\n        from pydantic import BaseModel\n\n        class Item(BaseModel):\n            name: str\n            description: str | None = None\n\n        app = FastAPI()\n        router = APIRouter()\n\n        @router.put("/items/{item_id}")\n        def replace_item(item_id: str, item: Item):\n            return {"message": "Item replaced", "id": item_id}\n\n        app.include_router(router)\n        ```\n        ';return A.api_route(path=path,response_model=response_model,status_code=status_code,tags=tags,dependencies=dependencies,summary=summary,description=description,response_description=response_description,responses=responses,deprecated=deprecated,methods=['PUT'],operation_id=operation_id,response_model_include=response_model_include,response_model_exclude=response_model_exclude,response_model_by_alias=response_model_by_alias,response_model_exclude_unset=response_model_exclude_unset,response_model_exclude_defaults=response_model_exclude_defaults,response_model_exclude_none=response_model_exclude_none,include_in_schema=include_in_schema,response_class=response_class,name=name,callbacks=callbacks,openapi_extra=openapi_extra,generate_unique_id_function=generate_unique_id_function)
	def post(A,path:R[T,Q(q)],*,response_model:R[W,Q(r)]=F(A),status_code:R[S[f],Q(s)]=A,tags:R[S[c[b[T,k]]],Q(t)]=A,dependencies:R[S[h[i.Depends]],Q(u)]=A,summary:R[S[T],Q(v)]=A,description:R[S[T],Q(w)]=A,response_description:R[T,Q(y)]=n,responses:R[S[Z[b[f,T],Z[T,W]]],Q(z)]=A,deprecated:R[S[V],Q(ª)]=A,operation_id:R[S[T],Q(µ)]=A,response_model_include:R[S[x],Q(º)]=A,response_model_exclude:R[S[x],Q(À)]=A,response_model_by_alias:R[V,Q(Á)]=d,response_model_exclude_unset:R[V,Q(Â)]=X,response_model_exclude_defaults:R[V,Q(Ã)]=X,response_model_exclude_none:R[V,Q(Ä)]=X,include_in_schema:R[V,Q(Å)]=d,response_class:R[j[C],Q(Ç)]=F(H),name:R[S[T],Q(È)]=A,callbacks:R[S[c[U]],Q(É)]=A,openapi_extra:R[S[Z[T,W]],Q(Ë)]=A,generate_unique_id_function:R[a[[m],T],Q(o)]=F(D)):'\n        Add a *path operation* using an HTTP POST operation.\n\n        ## Example\n\n        ```python\n        from fastapi import APIRouter, FastAPI\n        from pydantic import BaseModel\n\n        class Item(BaseModel):\n            name: str\n            description: str | None = None\n\n        app = FastAPI()\n        router = APIRouter()\n\n        @router.post("/items/")\n        def create_item(item: Item):\n            return {"message": "Item created"}\n\n        app.include_router(router)\n        ```\n        ';return A.api_route(path=path,response_model=response_model,status_code=status_code,tags=tags,dependencies=dependencies,summary=summary,description=description,response_description=response_description,responses=responses,deprecated=deprecated,methods=['POST'],operation_id=operation_id,response_model_include=response_model_include,response_model_exclude=response_model_exclude,response_model_by_alias=response_model_by_alias,response_model_exclude_unset=response_model_exclude_unset,response_model_exclude_defaults=response_model_exclude_defaults,response_model_exclude_none=response_model_exclude_none,include_in_schema=include_in_schema,response_class=response_class,name=name,callbacks=callbacks,openapi_extra=openapi_extra,generate_unique_id_function=generate_unique_id_function)
	def delete(A,path:R[T,Q(q)],*,response_model:R[W,Q(r)]=F(A),status_code:R[S[f],Q(s)]=A,tags:R[S[c[b[T,k]]],Q(t)]=A,dependencies:R[S[h[i.Depends]],Q(u)]=A,summary:R[S[T],Q(v)]=A,description:R[S[T],Q(w)]=A,response_description:R[T,Q(y)]=n,responses:R[S[Z[b[f,T],Z[T,W]]],Q(z)]=A,deprecated:R[S[V],Q(ª)]=A,operation_id:R[S[T],Q(µ)]=A,response_model_include:R[S[x],Q(º)]=A,response_model_exclude:R[S[x],Q(À)]=A,response_model_by_alias:R[V,Q(Á)]=d,response_model_exclude_unset:R[V,Q(Â)]=X,response_model_exclude_defaults:R[V,Q(Ã)]=X,response_model_exclude_none:R[V,Q(Ä)]=X,include_in_schema:R[V,Q(Å)]=d,response_class:R[j[C],Q(Ç)]=F(H),name:R[S[T],Q(È)]=A,callbacks:R[S[c[U]],Q(É)]=A,openapi_extra:R[S[Z[T,W]],Q(Ë)]=A,generate_unique_id_function:R[a[[m],T],Q(o)]=F(D)):'\n        Add a *path operation* using an HTTP DELETE operation.\n\n        ## Example\n\n        ```python\n        from fastapi import APIRouter, FastAPI\n\n        app = FastAPI()\n        router = APIRouter()\n\n        @router.delete("/items/{item_id}")\n        def delete_item(item_id: str):\n            return {"message": "Item deleted"}\n\n        app.include_router(router)\n        ```\n        ';return A.api_route(path=path,response_model=response_model,status_code=status_code,tags=tags,dependencies=dependencies,summary=summary,description=description,response_description=response_description,responses=responses,deprecated=deprecated,methods=['DELETE'],operation_id=operation_id,response_model_include=response_model_include,response_model_exclude=response_model_exclude,response_model_by_alias=response_model_by_alias,response_model_exclude_unset=response_model_exclude_unset,response_model_exclude_defaults=response_model_exclude_defaults,response_model_exclude_none=response_model_exclude_none,include_in_schema=include_in_schema,response_class=response_class,name=name,callbacks=callbacks,openapi_extra=openapi_extra,generate_unique_id_function=generate_unique_id_function)
	def options(A,path:R[T,Q(q)],*,response_model:R[W,Q(r)]=F(A),status_code:R[S[f],Q(s)]=A,tags:R[S[c[b[T,k]]],Q(t)]=A,dependencies:R[S[h[i.Depends]],Q(u)]=A,summary:R[S[T],Q(v)]=A,description:R[S[T],Q(w)]=A,response_description:R[T,Q(y)]=n,responses:R[S[Z[b[f,T],Z[T,W]]],Q(z)]=A,deprecated:R[S[V],Q(ª)]=A,operation_id:R[S[T],Q(µ)]=A,response_model_include:R[S[x],Q(º)]=A,response_model_exclude:R[S[x],Q(À)]=A,response_model_by_alias:R[V,Q(Á)]=d,response_model_exclude_unset:R[V,Q(Â)]=X,response_model_exclude_defaults:R[V,Q(Ã)]=X,response_model_exclude_none:R[V,Q(Ä)]=X,include_in_schema:R[V,Q(Å)]=d,response_class:R[j[C],Q(Ç)]=F(H),name:R[S[T],Q(È)]=A,callbacks:R[S[c[U]],Q(É)]=A,openapi_extra:R[S[Z[T,W]],Q(Ë)]=A,generate_unique_id_function:R[a[[m],T],Q(o)]=F(D)):'\n        Add a *path operation* using an HTTP OPTIONS operation.\n\n        ## Example\n\n        ```python\n        from fastapi import APIRouter, FastAPI\n\n        app = FastAPI()\n        router = APIRouter()\n\n        @router.options("/items/")\n        def get_item_options():\n            return {"additions": ["Aji", "Guacamole"]}\n\n        app.include_router(router)\n        ```\n        ';return A.api_route(path=path,response_model=response_model,status_code=status_code,tags=tags,dependencies=dependencies,summary=summary,description=description,response_description=response_description,responses=responses,deprecated=deprecated,methods=['OPTIONS'],operation_id=operation_id,response_model_include=response_model_include,response_model_exclude=response_model_exclude,response_model_by_alias=response_model_by_alias,response_model_exclude_unset=response_model_exclude_unset,response_model_exclude_defaults=response_model_exclude_defaults,response_model_exclude_none=response_model_exclude_none,include_in_schema=include_in_schema,response_class=response_class,name=name,callbacks=callbacks,openapi_extra=openapi_extra,generate_unique_id_function=generate_unique_id_function)
	def head(A,path:R[T,Q(q)],*,response_model:R[W,Q(r)]=F(A),status_code:R[S[f],Q(s)]=A,tags:R[S[c[b[T,k]]],Q(t)]=A,dependencies:R[S[h[i.Depends]],Q(u)]=A,summary:R[S[T],Q(v)]=A,description:R[S[T],Q(w)]=A,response_description:R[T,Q(y)]=n,responses:R[S[Z[b[f,T],Z[T,W]]],Q(z)]=A,deprecated:R[S[V],Q(ª)]=A,operation_id:R[S[T],Q(µ)]=A,response_model_include:R[S[x],Q(º)]=A,response_model_exclude:R[S[x],Q(À)]=A,response_model_by_alias:R[V,Q(Á)]=d,response_model_exclude_unset:R[V,Q(Â)]=X,response_model_exclude_defaults:R[V,Q(Ã)]=X,response_model_exclude_none:R[V,Q(Ä)]=X,include_in_schema:R[V,Q(Å)]=d,response_class:R[j[C],Q(Ç)]=F(H),name:R[S[T],Q(È)]=A,callbacks:R[S[c[U]],Q(É)]=A,openapi_extra:R[S[Z[T,W]],Q(Ë)]=A,generate_unique_id_function:R[a[[m],T],Q(o)]=F(D)):'\n        Add a *path operation* using an HTTP HEAD operation.\n\n        ## Example\n\n        ```python\n        from fastapi import APIRouter, FastAPI\n        from pydantic import BaseModel\n\n        class Item(BaseModel):\n            name: str\n            description: str | None = None\n\n        app = FastAPI()\n        router = APIRouter()\n\n        @router.head("/items/", status_code=204)\n        def get_items_headers(response: Response):\n            response.headers["X-Cat-Dog"] = "Alone in the world"\n\n        app.include_router(router)\n        ```\n        ';return A.api_route(path=path,response_model=response_model,status_code=status_code,tags=tags,dependencies=dependencies,summary=summary,description=description,response_description=response_description,responses=responses,deprecated=deprecated,methods=['HEAD'],operation_id=operation_id,response_model_include=response_model_include,response_model_exclude=response_model_exclude,response_model_by_alias=response_model_by_alias,response_model_exclude_unset=response_model_exclude_unset,response_model_exclude_defaults=response_model_exclude_defaults,response_model_exclude_none=response_model_exclude_none,include_in_schema=include_in_schema,response_class=response_class,name=name,callbacks=callbacks,openapi_extra=openapi_extra,generate_unique_id_function=generate_unique_id_function)
	def patch(A,path:R[T,Q(q)],*,response_model:R[W,Q(r)]=F(A),status_code:R[S[f],Q(s)]=A,tags:R[S[c[b[T,k]]],Q(t)]=A,dependencies:R[S[h[i.Depends]],Q(u)]=A,summary:R[S[T],Q(v)]=A,description:R[S[T],Q(w)]=A,response_description:R[T,Q(y)]=n,responses:R[S[Z[b[f,T],Z[T,W]]],Q(z)]=A,deprecated:R[S[V],Q(ª)]=A,operation_id:R[S[T],Q(µ)]=A,response_model_include:R[S[x],Q(º)]=A,response_model_exclude:R[S[x],Q(À)]=A,response_model_by_alias:R[V,Q(Á)]=d,response_model_exclude_unset:R[V,Q(Â)]=X,response_model_exclude_defaults:R[V,Q(Ã)]=X,response_model_exclude_none:R[V,Q(Ä)]=X,include_in_schema:R[V,Q(Å)]=d,response_class:R[j[C],Q(Ç)]=F(H),name:R[S[T],Q(È)]=A,callbacks:R[S[c[U]],Q(É)]=A,openapi_extra:R[S[Z[T,W]],Q(Ë)]=A,generate_unique_id_function:R[a[[m],T],Q(o)]=F(D)):'\n        Add a *path operation* using an HTTP PATCH operation.\n\n        ## Example\n\n        ```python\n        from fastapi import APIRouter, FastAPI\n        from pydantic import BaseModel\n\n        class Item(BaseModel):\n            name: str\n            description: str | None = None\n\n        app = FastAPI()\n        router = APIRouter()\n\n        @router.patch("/items/")\n        def update_item(item: Item):\n            return {"message": "Item updated in place"}\n\n        app.include_router(router)\n        ```\n        ';return A.api_route(path=path,response_model=response_model,status_code=status_code,tags=tags,dependencies=dependencies,summary=summary,description=description,response_description=response_description,responses=responses,deprecated=deprecated,methods=['PATCH'],operation_id=operation_id,response_model_include=response_model_include,response_model_exclude=response_model_exclude,response_model_by_alias=response_model_by_alias,response_model_exclude_unset=response_model_exclude_unset,response_model_exclude_defaults=response_model_exclude_defaults,response_model_exclude_none=response_model_exclude_none,include_in_schema=include_in_schema,response_class=response_class,name=name,callbacks=callbacks,openapi_extra=openapi_extra,generate_unique_id_function=generate_unique_id_function)
	def trace(A,path:R[T,Q(q)],*,response_model:R[W,Q(r)]=F(A),status_code:R[S[f],Q(s)]=A,tags:R[S[c[b[T,k]]],Q(t)]=A,dependencies:R[S[h[i.Depends]],Q(u)]=A,summary:R[S[T],Q(v)]=A,description:R[S[T],Q(w)]=A,response_description:R[T,Q(y)]=n,responses:R[S[Z[b[f,T],Z[T,W]]],Q(z)]=A,deprecated:R[S[V],Q(ª)]=A,operation_id:R[S[T],Q(µ)]=A,response_model_include:R[S[x],Q(º)]=A,response_model_exclude:R[S[x],Q(À)]=A,response_model_by_alias:R[V,Q(Á)]=d,response_model_exclude_unset:R[V,Q(Â)]=X,response_model_exclude_defaults:R[V,Q(Ã)]=X,response_model_exclude_none:R[V,Q(Ä)]=X,include_in_schema:R[V,Q(Å)]=d,response_class:R[j[C],Q(Ç)]=F(H),name:R[S[T],Q(È)]=A,callbacks:R[S[c[U]],Q(É)]=A,openapi_extra:R[S[Z[T,W]],Q(Ë)]=A,generate_unique_id_function:R[a[[m],T],Q(o)]=F(D)):'\n        Add a *path operation* using an HTTP TRACE operation.\n\n        ## Example\n\n        ```python\n        from fastapi import APIRouter, FastAPI\n        from pydantic import BaseModel\n\n        class Item(BaseModel):\n            name: str\n            description: str | None = None\n\n        app = FastAPI()\n        router = APIRouter()\n\n        @router.trace("/items/{item_id}")\n        def trace_item(item_id: str):\n            return None\n\n        app.include_router(router)\n        ```\n        ';return A.api_route(path=path,response_model=response_model,status_code=status_code,tags=tags,dependencies=dependencies,summary=summary,description=description,response_description=response_description,responses=responses,deprecated=deprecated,methods=['TRACE'],operation_id=operation_id,response_model_include=response_model_include,response_model_exclude=response_model_exclude,response_model_by_alias=response_model_by_alias,response_model_exclude_unset=response_model_exclude_unset,response_model_exclude_defaults=response_model_exclude_defaults,response_model_exclude_none=response_model_exclude_none,include_in_schema=include_in_schema,response_class=response_class,name=name,callbacks=callbacks,openapi_extra=openapi_extra,generate_unique_id_function=generate_unique_id_function)
	@Þ('\n        on_event is deprecated, use lifespan event handlers instead.\n\n        Read more about it in the\n        [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).\n        ')
	def on_event(self,event_type:R[T,Q('\n                The type of event. `startup` or `shutdown`.\n                ')]):
		'\n        Add an event handler for the router.\n\n        `on_event` is deprecated, use `lifespan` event handlers instead.\n\n        Read more about it in the\n        [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/#alternative-events-deprecated).\n        '
		def A(func:P):self.add_event_handler(event_type,func);return func
		return A