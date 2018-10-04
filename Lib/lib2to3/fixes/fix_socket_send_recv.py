'''
  Copyright 2018 Pranav Devarakonda

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

   Licensed to PSF under a Contributor Agreement.
'''

'''Fixer that changes send() and recv() methods of socket objects.
    sock.send('data') into sock.send(str.encode('data')) 


'''
__author__ = "Pranav Devarakonda <devarakondapranav@yahoo.com>"

#local imports
from .. import fixer_base
from ..fixer_util import Name, Call, RParen, LParen, Dot
from .. import patcomp




class FixSocketSendRecv(fixer_base.BaseFix):
    BM_compatible = True
    explicit = True #The user must ask for this fixer
    PATTERN = """
               
               power< obj=any+
               trailer< '.' method=('send' | 'recv') > args=trailer< '(' [any] ')' > tail=any*
                >
              """
    



    def transform(self, node, results):
        # If we're already wrapped in an eval() call, we're done.
        
        '''
        for key in results:
            print(str(key) + "=> " + str(results[key]) )
        print(node.children)
        new = node.clone()
        new.prefix = ""
        #return Name(results['method'], prefix=node.prefix)

        '''
        print(node.children)
        for key in results:
            print(str(key) + "=> " + str(results[key]))
            try:
                print(str(key) + "=> " + str(type(results[key][0])))
            except:
                pass

        if("modulename" in results):

            if(str(results["method"][0]) == "send"):
                for child in node.children:
                    if(False):
                        return
                node.insert_child(2, LParen())
                node.insert_child(3, Name("str.encode"))
                node.append_child(RParen())
                node.changed()
            else:
                node.append_child(Dot())
                node.append_child(Call(Name("decode"), [Name("'utf-8'")]))
                node.changed()



        #root = Name(str(results["obj"][0]))

        #return Call(Name(str(results["obj"][0])), [new], prefix=node.prefix)
