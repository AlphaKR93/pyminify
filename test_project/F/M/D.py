L=True
J=False
I=None
H=int
F=''
E=Exception
B=str
import html as D,inspect as M,traceback as N
from F.B import G
from F.F import Æ
from F.N import Y
from F.O import X,K
from F.V import Ê,A,Ì,Ò,Ñ,Send
O='\np {\n    color: #211c1c;\n}\n.traceback-container {\n    border: 1px solid #038BB8;\n}\n.traceback-title {\n    background-color: #038BB8;\n    color: lemonchiffon;\n    padding: 12px;\n    font-size: 20px;\n    margin-top: 0px;\n}\n.frame-line {\n    padding-left: 10px;\n    font-family: monospace;\n}\n.frame-filename {\n    font-family: monospace;\n}\n.center-line {\n    background-color: #038BB8;\n    color: #f9f6e1;\n    padding: 5px 0px 5px 5px;\n}\n.lineno {\n    margin-right: 5px;\n}\n.frame-title {\n    font-weight: unset;\n    padding: 10px 10px 10px 10px;\n    background-color: #E4F4FD;\n    margin-right: 10px;\n    color: #191f21;\n    font-size: 17px;\n    border: 1px solid #c7dce8;\n}\n.collapse-btn {\n    float: right;\n    padding: 0px 5px 1px 5px;\n    border: solid 1px #96aebb;\n    cursor: pointer;\n}\n.collapsed {\n  display: none;\n}\n.source-code {\n  font-family: courier;\n  font-size: small;\n  padding-bottom: 10px;\n}\n'
P='\n<script type="text/javascript">\n    function collapse(element){\n        const frameId = element.getAttribute("data-frame-id");\n        const frame = document.getElementById(frameId);\n\n        if (frame.classList.contains("collapsed")){\n            element.innerHTML = "&#8210;";\n            frame.classList.remove("collapsed");\n        } else {\n            element.innerHTML = "+";\n            frame.classList.add("collapsed");\n        }\n    }\n</script>\n'
Q='\n<html>\n    <head>\n        <style type=\'text/css\'>\n            {styles}\n        </style>\n        <title>Starlette Debugger</title>\n    </head>\n    <body>\n        <h1>500 Server Error</h1>\n        <h2>{error}</h2>\n        <div class="traceback-container">\n            <p class="traceback-title">Traceback</p>\n            <div>{exc_html}</div>\n        </div>\n        {js}\n    </body>\n</html>\n'
R='\n<div>\n    <p class="frame-title">File <span class="frame-filename">{frame_filename}</span>,\n    line <i>{frame_lineno}</i>,\n    in <b>{frame_name}</b>\n    <span class="collapse-btn" data-frame-id="{frame_filename}-{frame_lineno}" onclick="collapse(this)">{collapse_button}</span>\n    </p>\n    <div id="{frame_filename}-{frame_lineno}" class="source-code {collapsed}">{code_context}</div>\n</div>\n'
S='\n<p><span class="frame-line">\n<span class="lineno">{lineno}.</span> {line}</span></p>\n'
T='\n<p class="center-line"><span class="frame-line center-line">\n<span class="lineno">{lineno}.</span> {line}</span></p>\n'
class Z:
	def __init__(A,app:Ê,handler:A|I=I,debug:bool=J):A.app=app;A.handler=handler;A.debug=debug
	async def __call__(A,scope:Ñ,receive:Ò,send:Send):
		N='type';K=receive;D=send;B=scope
		if B[N]!='http':await A.app(B,K,D);return
		M=J
		async def O(message:Ì):
			A=message;nonlocal M,D
			if A[N]=='http.response.start':M=L
			await D(A)
		try:await A.app(B,K,O)
		except E as C:
			F=Y(B)
			if A.debug:H=A.debug_response(F,C)
			elif A.handler is I:H=A.error_response(F,C)
			elif G(A.handler):H=await A.handler(F,C)
			else:H=await Æ(A.handler,F,C)
			if not M:await H(B,K,D)
			raise C
	def format_line(E,index:H,line:B,frame_lineno:H,frame_index:H):
		B=frame_index;A=index;C={'line':D.escape(line).replace(' ','&nbsp'),'lineno':frame_lineno-B+A}
		if A!=B:return S.format(**C)
		return T.format(**C)
	def generate_frame_html(E,frame:M.FrameInfo,is_collapsed:bool):C='collapsed';B=is_collapsed;A=frame;G=F.join(E.format_line(B,C,A.lineno,A.index)for(B,C)in enumerate(A.code_context or[]));H={'frame_filename':D.escape(A.filename),'frame_lineno':A.lineno,'frame_name':D.escape(A.function),'code_context':G,C:C if B else F,'collapse_button':'+'if B else'&#8210;'};return R.format(**H)
	def generate_html(K,exc:E,limit:H=7):
		A=N.TracebackException.from_exception(exc,capture_locals=L);C=F;E=J;G=exc.__traceback__
		if G is not I:
			R=M.getinnerframes(G,limit)
			for S in reversed(R):C+=K.generate_frame_html(S,E);E=L
		H=A.exc_type.__name__;T=f"{D.escape(H)}: {D.escape(B(A))}";return Q.format(styles=O,js=P,error=T,exc_html=C)
	def generate_plain_text(B,exc:E):A=exc;return F.join(N.format_exception(type(A),A,A.__traceback__))
	def debug_response(B,request:Y,exc:E):
		C=request.headers.get('accept',F)
		if'text/html'in C:A=B.generate_html(exc);return X(A,status_code=500)
		A=B.generate_plain_text(exc);return K(A,status_code=500)
	def error_response(A,request:Y,exc:E):return K('Internal Server Error',status_code=500)