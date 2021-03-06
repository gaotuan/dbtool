�
���^c           @   se  d  d l  m Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l m Z d dT d �  �  YZ d d d � Z d �  Z d	 �  Z d
 �  Z d �  Z d �  Z d �  Z e d k rad Z e	 j d d d d d d d d � Z e j d d d e d e d d d d �e j d  d! d e d e d d" d d# �e j d$ d% d e d e d d& d d' �e j d( d) d e d e d d* d d+ �e j d, d- d e d e d d* d d. �e j d/ d0 d e d e d d" d d1 �e j d2 d3 d e d e d d* d d4 �e j d5 d6 d e d e d d* d d7 �e j d8 d9 d e d e d d* d d: �e j d; d< d e d e d d* d d= �e j d> d? d@ dA d e d dB �e j dC dD d@ dA d e d dE �e j dF dG d@ dA d e d dH �e j  �  Z! e! j" Z" e! j# Z# e! j$ Z$ e! j% Z% e! j& Z& e! j' Z' e! j( Z( e! j) Z) e! j* Z+ e! j, Z- e! j. Z/ e! j0 Z1 e! j2 Z2 e dI � Z3 e a4 e
 j
 e
 j5 e � e
 j
 e
 j6 e � e
 j
 e
 j7 e � e e" e# e$ e% � \ Z8 Z9 Z: Z; Z< e e< e+ e- e/ e1 � \ Z= Z> Z? Z@ ZA dJ ZB dK ZC eC GHe& d* k r�e& jD dL � ZE eF eE � dM k r~dN e& ZG n e eH eE � � ZG dO eB eG f ZB n  e) d* k re) jD dL � ZI eF eI � dM k r�dN e) ZJ n e eH eI � � ZJ dP eB eJ f ZB n  dQ eB ZB e( r$e< jK eB � ZL n e< jK eB � ZL x# eL D] ZM e eM dR eM dS � q:WeC GHn  d S(U   i����(   t   divisionN(   t   Poolt   dbconnc           B   s#   e  Z d  �  Z d �  Z d �  Z RS(   c         C   s�   | |  _  | |  _ | |  _ | |  _ | |  _ y/ |  j �  |  _ |  j j |  j � t |  _	 Wn4 t
 k
 r� } t |  _	 d | |  j  |  j f GHn Xd  S(   Ns)   Connect mysql error: %s,server ip：%s:%s(   t   db_hostt   db_portt   db_usert	   db_passwdt	   db_dbnamet   getConnectiont   connt	   select_dbt   Truet   succt	   Exceptiont   False(   t   selft   hostt   portt   usert   passwdt   dbnamet   error(    (    s   j.pyt   __init__   s    						c         C   sL   t  j d |  j d |  j d |  j d t |  j � d d d d d	 t  j j � S(
   NR   R   R   R   t   connect_timeouti   t   charsett   utf8t   cursorclass(	   t   MySQLdbt   connectR   R   R   t   intR   t   cursorst
   DictCursor(   R   (    (    s   j.pyR      s    c         C   sV   yG |  j  j �  } | j | � | j �  } | j �  |  j  j �  | SWn d  SXd  S(   N(   R	   t   cursort   executet   fetchallt   closet   commit(   R   t   sqlR    t   data(    (    s   j.pyt   myquery   s    
(   t   __name__t
   __module__R   R   R'   (    (    (    s   j.pyR      s   		t   debugc         C   s�   i t  j d 6t  j d 6t  j d 6t  j d 6t  j d 6} t  j �  } | d  k re t  j t	 j
 � } n t  j j | d d d d	 �} t  j d
 d � } | j | � | j | � | j | |  � | S(   NR*   t   infoR   t   warningt   criticalt   maxBytesi   t   backupCounti   s1   %(asctime) s%(lineno)5d %(levelname)s %(message)ss   %Y-%m-%d %H:%M:%S(   t   loggingt   DEBUGt   INFOt   ERRORt   WARNINGt   CRITICALt	   getLoggert   Nonet   StreamHandlert   syst   stderrt   handlerst   RotatingFileHandlert	   Formattert   setFormattert
   addHandlert   setLevel(   t   Levelt   LOG_FILEt   Loglevelt   loggert   hdlrt	   formatter(    (    s   j.pyRD   (   s    !c      	   C   s�  | d k s$ | d k s$ | d k r,|  j  d � } | d d } | d d } | d d } |  j  d � d d }	 |	 j d	 � r� |  j  d
 � d d }
 d |
 } n | d d } d | } yC t j j | � r� t j | � d } n |  j  d � d d } WqDt k
 r(} t j	 d | � qDXn | } | } | } | } t
 | | | | t � } | j  d � d d } d | | | | | | f } | GHd } | GH| | | | | f S(   s!   获取master密码及master连接t    s   show slave statusi    t   Master_Hostt   Master_Portt   Master_Users   select version() as versiont   versions   5.5s   show variables like "datadir"t   Values   %s/master.infot   Master_Info_Files   sed -n '6p' %si   s1   select User_password from mysql.slave_master_infot   User_passwords   get master password error: %ssW   select substring_index(host,':',1) as myip  from PROCESSLIST  where ID=CONNECTION_ID();t   myipsm   Master:%s %s , Slave need privilege:
    grant select on *.* to %s@'%s'
    revoke select on *.* from %s.'%s's�       Tip: ma是主,sl是从.delay是查询结束后从库的延迟.Count:-2表示读错误,-1表示表不存在.diff:*主从有一边不存在表,error查询过程出现错误.
(   R'   t
   startswitht   ost   patht   isfilet   commandst   getstatusoutputR   t   lgR+   R   R   (   t   myconnt   masterhost2t   masterport2t   masteruser2t   masterpassword2t	   slaveinfot
   masterhostt
   masterportt
   masteruserRK   t   datadirt   passwordfilet   cmdt   masterpasswordR   t
   masterconnRO   t   msgt   mymsg(    (    s   j.pyt   get_masterinfo6   s8    $
c         C   s�   yp d } |  j  | � } xT | D]L } d j | d | d � } |  j  | � t j d | d | d f � q WWn$ t k
 r� } t j d | � n Xd S(   sK   每次检查操作的时候检查slave repl账号是否有 Show view 权限s   select user,host from mysql.user where (Show_view_priv='N' or Select_priv='N' or Reload_priv='N' ) and user in ('slave','repl')s1   grant Show view,select,Reload on *.* to "{}"@"{}"R   R   s   grant privileges %s@%s succs   grant privileges error: %sN(   R'   t   formatRV   R+   R   (   RW   t   select_user_sqlt   select_usert   onet   grantpri_sqlR   (    (    s   j.pyt	   grant_priZ   s    'c         C   s   t  a t j d � d  S(   Ns   Catched interrupt signal.Exit!(   R   t   is_sigint_upRV   R+   (   t   signumt   frame(    (    s   j.pyt   sigint_handlerf   s    c         C   s�   y_ t  |  t | � | | d � } | j sK t j d |  | f � t d f S|  | | | | f SWn$ t k
 r� } t j d | � n Xd  S(   Nt   information_schemas   mysql %s:%s link errorRG   s   get_slaveinfo exec error: %s(   R   R   R   RV   R+   R   R   (   t	   slavehostt	   slaveportt	   slaveusert   slavepasswordRW   R   (    (    s   j.pyt   get_slaveinfok   s    	
c         C   s�  y�t  |  | | | d � } t r1 | j d � n | j d � d | | f } | j | � } t | � d k r� i d d 6d d	 6d d
 6d d 6d d 6S| d d }	 d | | f }
 t j d t j t j �  � � } | j |
 � } t j d t j t j �  � � } t rg  } n | j d � } t | � d k rF| d d } n d } i | d d d 6| d	 6| d
 6|	 d 6| d 6S| j j	 �  Wn7 t
 k
 r�} i d d 6d d	 6d d
 6d d 6d d 6SXd  S(   NRr   s$   set tx_isolation='READ-UNCOMMITTED';s"   set tx_isolation='READ-COMMITTED';sX   select ENGINE from information_schema.TABLES where TABLE_SCHEMA='%s' and TABLE_NAME='%s'i    i����t   countRG   t   startt   endt   enginet   delayt   ENGINEs$   select count(*) as count from %s.%s s   %H:%M:%Ss   show slave statusi   t   Seconds_Behind_Masteri����(   R   t   uncommitreadR'   t   lent   timet   strftimet	   localtimet   nodelayR	   R#   R   (   R   R   R   t   passwordR   t	   tablenameRW   t   table_exists_sqlt   table_existsR{   t   table_count_sqlRy   t   table_countRz   t   curslaveinfoR|   R   (    (    s   j.pyR�   v   s0    '!!	/c         C   s�  t  r t j d � n  t d d � } i  } | j t d t t t t	 |  | f �| d <| j t d t
 t t t |  | f �| d <| j �  | j �  | d j �  d } | d j �  d } | d j �  d	 } | d j �  d
 } | d j �  d } | d j �  d }	 | d j �  d }
 | d j �  d	 } | d j �  d
 } d |  | f } | d k sq|	 d k rzd } n+ | d k s�|	 d k r�d } n
 |	 | } d | | | |
 | | | | |	 | | f } | GH| j �  d S(   s$   difference between slave and master i    t	   processesi   t   argst   slavet   masterRx   Ry   Rz   R{   R|   s   %s.%si����R   i����t   *s>   %-40s |%-9s %-9s|%-8s %-8s |%-8s %-8s |%-7s|%-15s %-15s |%-10sN(   Rn   RQ   t   _exitR   t   apply_asyncR�   t   myhostt   myportt   myusert
   mypasswordt   mahostt   maportt   mausert
   mapasswordR#   t   joint   gett   clear(   R   R�   t   poolt   resultt   slcountt   slstartt   slendt   slenginet   sldelayt   macountt   mastartt   maendt   maenginet   dbtablet   markRe   (    (    s   j.pyt   diff_pro�   s4    ++

		
+t   __main__Rr   t   descriptions�   ******************2个MySQL表记录数比对(默认主从)******************
(默认alldb,除了information_schema,performance_schema,auditdb和View)t   epilogs   by van 2017RK   s   2.1t   usageso   -sh 127.0.0.1 -sp 3307 -su db_monitor -sa xxxx   -mh 192.168.1.5 -mp 3306 -mu db_monitor -ma xxxx -db db_name  s   -shs   --slavehostt   typet   requiredt   defaults	   127.0.0.1t   helps   从节点 ips   -sps   --slaveporti�  s   从节点ports   -sus   --slaveusert   roots   从节点users   -sas   --slavepasswordRG   s   从节点密码s   -mhs   --masterhostsP   在不使用slave自动获取master连接的情况下,可以指定主节点的ips   -mps   --masterports   主节点ports   -mus   --masterusers   主节点users   -mas   --masterpasswords   主节点密码s   -dbs   --perdbs   指定database,eg:'db1,db2's   -tbs
   --pertables   指定table,eg:'tab1,tab2's   -sls   --slavefirstt   actiont
   store_trues9   指定比对时候以slave为主,默认是以master为主s   -urs   --uncommitreadsH   使用未提交读隔离级别:READ-UNCOMMITTED,默认是:READ-COMMITTEDs   -nds	   --nodelays(   指定不检查slave delay,tidb要指定R+   s�   select TABLE_SCHEMA,TABLE_NAME from information_schema.TABLES where TABLE_SCHEMA not in ('information_schema','performance_schema','auditdb') and TABLE_TYPE='BASE TABLE's�   --dbName.tableName-----------------------|maEngine-slEngine--|maStart--slStart--|maEnd----slEnd----|delay--|maCount---------slCount---------|difft   ,i   s   ('%s')s   %s and TABLE_SCHEMA in  %ss   %s and TABLE_NAME in %ss#   %s order by TABLE_SCHEMA,TABLE_NAMEt   TABLE_SCHEMAt
   TABLE_NAME(    (N   t
   __future__R    t   MySQLdb.cursorsR   RQ   R9   t   reR�   RT   t   argparset   signalR0   t   logging.handlerst   multiprocessing.poolR   R   R7   RD   Rg   Rm   Rq   Rw   R�   R�   R(   R   t   ArgumentParsert   parsert   add_argumentt   strR   R   t
   parse_argsR�   Rs   Rt   Ru   Rv   t   perdbR   t
   slavefirstt   pertableR]   RX   R^   RY   R_   RZ   Rc   R[   R�   RV   Rn   t   SIGINTt   SIGHUPt   SIGTERMR�   R�   R�   R�   RW   R�   R�   R�   R�   t   maconnt   pertable_sqlt   titlet   splitt
   perdbsplitR�   t	   perdblistt   tuplet   pertablesplitt   pertablelistR'   t   alltableRk   (    (    (    s   j.pyt   <module>   s�   0	$							(((((((((("""													$'
