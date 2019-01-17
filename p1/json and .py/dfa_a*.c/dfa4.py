import argparse
import json
parser = argparse.ArgumentParser(description="This is about 'a*.c' simple DFA implementation. The DFA definition is specified via .dfa file; input string is read from stdin. In non-verbose mode,print Accept or Not ACCEPT as the case may be. Remind: in machine definition, 'E' stands for all the alphabet",epilog="*******use the command: python3 dfa4.py -d m4.dfa -v*******alpabet is all the symbols ") 
  
parser.add_argument('-d', action='store', dest='dfafile', default=None, help="DFA definition File,in definition file,'E' stands for all the alphabet", required=True)  
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
         q=str(w)
         print(q)
         str_len=len(q)
         flag_str=0
         if(q[0]!="a"):
                    print(' Current State: '+cu_state+' Symbol: '+q[0]+' ---->New State: '+'q5')
                    for i in q[1:]:
                           print(' Current State: '+'q5'+' Symbol: '+i+' ---->New State: '+'q5')
         else:
                    print(' Current State: '+cu_state+' Symbol: '+q[0]+' ---->New State: '+'q2')
                    temp=1
                    for i in q[1:str_len]:
                           temp=temp+1
                           if(q[temp-1]!="."):
                                   print(' Current State: '+'q2'+' Symbol: '+i+' ---->New State: '+'q2')
                                   
                           else:
                                   print(' Current State: '+'q2'+' Symbol: '+i+' ---->New State: '+'q3')
                                   if(temp==(str_len-1)):
                                            if(q[str_len-1]=="c"):
                                                 print(' Current State: '+'q3'+' Symbol: '+q[str_len-1]+' ---->New State: '+'q4')
                                                 flag_str=1
                                                 break
                                            else:
                                                 print(' Current State: '+'q3'+' Symbol: '+q[str_len-1]+' ---->New State: '+'q5')
                                                 break
                                   else:
                                            
                                            print(' Current State: '+'q3'+' Symbol: '+q[temp-1]+' ---->New State: '+'q5')
                                            break
 
                    
                                   for i in q[temp+1:str_len]:
                                            print(' Current State: '+'q5'+' Symbol: '+i+' ---->New State: '+'q5')
         if(flag_str==1):
                print('String: '+ q +'---->''Accepted')
         else:
                print('String: '+ q + '---->''not accepted')
else:
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
         q=str(w)
         print(q)
         str_len=len(q)
         flag_str=0
         if(q[0] == "a"):                    
                    temp=1
                    for i in q[1:str_len]:
                           temp=temp+1
                           if(q[temp-1]=="."):                                   
                                   if(temp==(str_len-1)):
                                            if(q[str_len-1]=="c"):
                                                 
                                                 flag_str=1
                                                 break
                                            else:
                                                 
                                                 break
                                   else:
                                           
                                            break                   
                                   
         if(flag_str==1):
                print('String: '+ q +'---->''Accepted')
         else:
                print('String: '+ q + '---->''not accepted')
