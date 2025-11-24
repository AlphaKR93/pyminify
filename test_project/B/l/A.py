µ='ISO-8859-3'
ª='IBM866'
z='Vietnamese'
y='Turkish'
x='Thai'
w='Serbian'
v='Slovene'
u='Slovak'
t='Russian'
s='Romanian'
r='Portuguese'
q='Polish'
p='Dutch'
o='Macedonian'
n='Latvian'
m='Lithuanian'
l='Italian'
k='Hungarian'
j='Croatian'
i='Hebrew'
h='French'
g='Finnish'
f='Estonian'
e='Spanish'
d='Esperanto'
c='English'
b='Greek'
a='German'
Z='Danish'
Y='Czech'
X='Bulgarian'
W='Belarusian'
V='Arabic'
S='WINDOWS-1257'
R='ISO-8859-13'
Q='ISO-8859-4'
P='IBM855'
O='MacCyrillic'
N='WINDOWS-1251'
M='ISO-8859-5'
K=None
J=str
I='ISO-8859-15'
H='WINDOWS-1250'
G='ISO-8859-2'
F='MacRoman'
E='WINDOWS-1252'
D='ISO-8859-1'
C=True
B=False
from string import ascii_letters as T
from typing import List as U,Optional as L
class A:
	def __init__(A,name:L[J]=K,iso_code:L[J]=K,use_ascii:bool=C,charsets:L[U[J]]=K,alphabet:L[J]=K,wiki_start_pages:L[U[J]]=K):
		B=alphabet;super().__init__();A.name=name;A.iso_code=iso_code;A.use_ascii=use_ascii;A.charsets=charsets
		if A.use_ascii:
			if B:B+=T
			else:B=T
		elif not B:raise ValueError('Must supply alphabet if use_ascii is False')
		A.alphabet=''.join(sorted(set(B)))if B else K;A.wiki_start_pages=wiki_start_pages
	def __repr__(A):B=', '.join(f"{A}={B!r}"for(A,B)in A.__dict__.items()if not A.startswith('_'));return f"{A.__class__.__name__}({B})"
º={V:A(name=V,iso_code='ar',use_ascii=B,charsets=['ISO-8859-6','WINDOWS-1256','CP720','CP864'],alphabet='ءآأؤإئابةتثجحخدذرزسشصضطظعغػؼؽؾؿـفقكلمنهوىيًٌٍَُِّ',wiki_start_pages=['الصفحة_الرئيسية']),W:A(name=W,iso_code='be',use_ascii=B,charsets=[M,N,ª,O],alphabet='АБВГДЕЁЖЗІЙКЛМНОПРСТУЎФХЦЧШЫЬЭЮЯабвгдеёжзійклмнопрстуўфхцчшыьэюяʼ',wiki_start_pages=['Галоўная_старонка']),X:A(name=X,iso_code='bg',use_ascii=B,charsets=[M,N,P],alphabet='АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЬЮЯабвгдежзийклмнопрстуфхцчшщъьюя',wiki_start_pages=['Начална_страница']),Y:A(name=Y,iso_code='cz',use_ascii=C,charsets=[G,H],alphabet='áčďéěíňóřšťúůýžÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ',wiki_start_pages=['Hlavní_strana']),Z:A(name=Z,iso_code='da',use_ascii=C,charsets=[D,I,E,F],alphabet='æøåÆØÅ',wiki_start_pages=['Forside']),a:A(name=a,iso_code='de',use_ascii=C,charsets=[D,I,E,F],alphabet='äöüßẞÄÖÜ',wiki_start_pages=['Wikipedia:Hauptseite']),b:A(name=b,iso_code='el',use_ascii=B,charsets=['ISO-8859-7','WINDOWS-1253'],alphabet='αβγδεζηθικλμνξοπρσςτυφχψωάέήίόύώΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΣΤΥΦΧΨΩΆΈΉΊΌΎΏ',wiki_start_pages=['Πύλη:Κύρια']),c:A(name=c,iso_code='en',use_ascii=C,charsets=[D,E,F],wiki_start_pages=['Main_Page']),d:A(name=d,iso_code='eo',use_ascii=B,charsets=[µ],alphabet='abcĉdefgĝhĥijĵklmnoprsŝtuŭvzABCĈDEFGĜHĤIJĴKLMNOPRSŜTUŬVZ',wiki_start_pages=['Vikipedio:Ĉefpaĝo']),e:A(name=e,iso_code='es',use_ascii=C,charsets=[D,I,E,F],alphabet='ñáéíóúüÑÁÉÍÓÚÜ',wiki_start_pages=['Wikipedia:Portada']),f:A(name=f,iso_code='et',use_ascii=B,charsets=[Q,R,S],alphabet='ABDEGHIJKLMNOPRSTUVÕÄÖÜabdeghijklmnoprstuvõäöü',wiki_start_pages=['Esileht']),g:A(name=g,iso_code='fi',use_ascii=C,charsets=[D,I,E,F],alphabet='ÅÄÖŠŽåäöšž',wiki_start_pages=['Wikipedia:Etusivu']),h:A(name=h,iso_code='fr',use_ascii=C,charsets=[D,I,E,F],alphabet='œàâçèéîïùûêŒÀÂÇÈÉÎÏÙÛÊ',wiki_start_pages=['Wikipédia:Accueil_principal','Bœuf (animal)']),i:A(name=i,iso_code='he',use_ascii=B,charsets=['ISO-8859-8','WINDOWS-1255'],alphabet='אבגדהוזחטיךכלםמןנסעףפץצקרשתװױײ',wiki_start_pages=['עמוד_ראשי']),j:A(name=j,iso_code='hr',use_ascii=B,charsets=[G,H],alphabet='abcčćdđefghijklmnoprsštuvzžABCČĆDĐEFGHIJKLMNOPRSŠTUVZŽ',wiki_start_pages=['Glavna_stranica']),k:A(name=k,iso_code='hu',use_ascii=B,charsets=[G,H],alphabet='abcdefghijklmnoprstuvzáéíóöőúüűABCDEFGHIJKLMNOPRSTUVZÁÉÍÓÖŐÚÜŰ',wiki_start_pages=['Kezdőlap']),l:A(name=l,iso_code='it',use_ascii=C,charsets=[D,I,E,F],alphabet='ÀÈÉÌÒÓÙàèéìòóù',wiki_start_pages=['Pagina_principale']),m:A(name=m,iso_code='lt',use_ascii=B,charsets=[R,S,Q],alphabet='AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽaąbcčdeęėfghiįyjklmnoprsštuųūvzž',wiki_start_pages=['Pagrindinis_puslapis']),n:A(name=n,iso_code='lv',use_ascii=B,charsets=[R,S,Q],alphabet='AĀBCČDEĒFGĢHIĪJKĶLĻMNŅOPRSŠTUŪVZŽaābcčdeēfgģhiījkķlļmnņoprsštuūvzž',wiki_start_pages=['Sākumlapa']),o:A(name=o,iso_code='mk',use_ascii=B,charsets=[M,N,O,P],alphabet='АБВГДЃЕЖЗЅИЈКЛЉМНЊОПРСТЌУФХЦЧЏШабвгдѓежзѕијклљмнњопрстќуфхцчџш',wiki_start_pages=['Главна_страница']),p:A(name=p,iso_code='nl',use_ascii=C,charsets=[D,E,F],wiki_start_pages=['Hoofdpagina']),q:A(name=q,iso_code='pl',use_ascii=B,charsets=[G,H],alphabet='AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻaąbcćdeęfghijklłmnńoóprsśtuwyzźż',wiki_start_pages=['Wikipedia:Strona_główna']),r:A(name=r,iso_code='pt',use_ascii=C,charsets=[D,I,E,F],alphabet='ÁÂÃÀÇÉÊÍÓÔÕÚáâãàçéêíóôõú',wiki_start_pages=['Wikipédia:Página_principal']),s:A(name=s,iso_code='ro',use_ascii=C,charsets=[G,H],alphabet='ăâîșțĂÂÎȘȚ',wiki_start_pages=['Pagina_principală']),t:A(name=t,iso_code='ru',use_ascii=B,charsets=[M,N,'KOI8-R',O,ª,P],alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',wiki_start_pages=['Заглавная_страница']),u:A(name=u,iso_code='sk',use_ascii=C,charsets=[G,H],alphabet='áäčďéíĺľňóôŕšťúýžÁÄČĎÉÍĹĽŇÓÔŔŠŤÚÝŽ',wiki_start_pages=['Hlavná_stránka']),v:A(name=v,iso_code='sl',use_ascii=B,charsets=[G,H],alphabet='abcčdefghijklmnoprsštuvzžABCČDEFGHIJKLMNOPRSŠTUVZŽ',wiki_start_pages=['Glavna_stran']),w:A(name=w,iso_code='sr',alphabet='АБВГДЂЕЖЗИЈКЛЉМНЊОПРСТЋУФХЦЧЏШабвгдђежзијклљмнњопрстћуфхцчџш',charsets=[M,N,O,P],wiki_start_pages=['Главна_страна']),x:A(name=x,iso_code='th',use_ascii=B,charsets=['ISO-8859-11','TIS-620','CP874'],alphabet='กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮฯะัาำิีึืฺุู฿เแโใไๅๆ็่้๊๋์ํ๎๏๐๑๒๓๔๕๖๗๘๙๚๛',wiki_start_pages=['หน้าหลัก']),y:A(name=y,iso_code='tr',use_ascii=B,charsets=[µ,'ISO-8859-9','WINDOWS-1254'],alphabet='abcçdefgğhıijklmnoöprsştuüvyzâîûABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZÂÎÛ',wiki_start_pages=['Ana_Sayfa']),z:A(name=z,iso_code='vi',use_ascii=B,charsets=['WINDOWS-1258'],alphabet='aăâbcdđeêghiklmnoôơpqrstuưvxyAĂÂBCDĐEÊGHIKLMNOÔƠPQRSTUƯVXY',wiki_start_pages=['Chữ_Quốc_ngữ'])}