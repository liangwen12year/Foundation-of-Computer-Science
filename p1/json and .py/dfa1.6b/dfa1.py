import argparse
import json
parser = argparse.ArgumentParser(description="This is about 'HW2 1.6c' simple DFA implementation. The DFA definition is specified via .dfa file; input string is read from stdin. In non-verbose mode,print Accept or Not ACCEPT as the case may be",epilog="*******use the command: python3 dfa1.py -d m1.dfa -v*******alpabet is {0,1} ") 
#parser.add_argument('-h', action='store',help="print usage", required=False) 
parser.add_argument('-d', action='store', dest='dfafile', default=None, help="DFA definition File", required=True)  
parser.add_argument('-v', action='store_true',dest='file', help="verbose mode;display machine definition,transition etc.", required=False)    
args = parser.parse_args()
if (args.file): 
     with open(args.dfafile) as j_data:
        data=json.load(j_data)
     
     print('--------------------Begin definition------------------')
     print (json.dumps(data, sort_keys=True, indent=2))
     print('--------------------End definition------------------')

     while(True):
         l=len(data['transition'])
         cu_state=data['start_state']
         b=data['transition']
         last=data['final_states']
         lis=[]
         flag=1
         w=input('')
         #w=print(w)
         q=str(w)
         print(q)

         def spot(q,w):
            for i in range(l):
               if b[i]['current_state'] == q:
                  if b[i]['next_symbol'] == w:
                     cu_state= b[i]['new_state']
                     print(' Current State: '+q+' Symbol: '+w+' ---->New State: '+cu_state)
                     lis.append(cu_state)
                     return cu_state
	 
       

         for i in q:
            if(i!="0" and i!="1") : 
               print('Invalid alphabet:'+ i+'      igonre rest of string  ' + q)
               flag=0
               break
            cu_state=spot(cu_state,i)
	  
         if(flag==0):
               print( ' String: '+ q +'----->' + ' not accepted ')  
         elif(lis[-1] == last):
               print( ' String: '+ q +' -----> ' + '  accepted ')
         else:
               print( ' String: '+ q +'----->' + ' not accepted ')

         #if (lis[-1] == last and flag == 1):
           # print( ' String: '+ q +'----->' + ' accepted ')  
         #else:
          #  print( ' String: '+ q +' -----> ' + ' not accepted ')
	     
 		
else:
   with open(args.dfafile) as j_data:
    data=json.load(j_data)
  
	
   
   print('--------------------Begin definition------------------')
   
   print (json.dumps(data, sort_keys=True, indent=2))
   print('--------------------End definition------------------')

   def spot(q,w):
     for i in range(l):
        if b[i]['current_state'] == q:
           if b[i]['next_symbol'] == w:
                cu_state= b[i]['new_state']
                lis.append(cu_state)
	        #print(lis[0])
                return cu_state

   while(True):
      l=len(data['transition'])
      cu_state=data['start_state']
      b=data['transition']
      last=data['final_states']
      lis=[]
      flag=1
      w=input('')
      q=str(w)
      print(q)
 
	
      for i in q:
          if(i!="0" and i!="1") : 
               print('   Invalid alphabet:'+ i +'      igonre rest of string   ' + q)
               flag=0
               break
          cu_state=spot(cu_state,i)
 
      if(flag==0):
            print( ' String: '+ q +'----->' + ' not accepted ')  
      elif(lis[-1] == last):
            print( ' String: '+ q +' -----> ' + '  accepted ')
      else:
            print( ' String: '+ q +'----->' + ' not accepted ') 
      #if (lis[-1] == last and flag==1):
        # print( 'String:'+q+'----->'+ ' accepted')
    #  else:
        # print( 'String:'+q+'----->'+ 'not accepted')

