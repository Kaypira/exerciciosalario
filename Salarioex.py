s1 = float(input('digite o seu salario '))
if s1 < 280.00:
    sa1 = s1 * 1.20
    au1 = sa1 - s1
    inf1 = sa1 * 0.962
    print (f'_o salario antes era {s1} _o percentual aplicado foi 20% _o valor do aumento foi {au1} _o novo salario apos o aumento é {sa1}  _o valor descontado a inflaçao é {inf1}')
   
elif s1 > 280.00 and s1 < 700.00 :
    sa1 = s1 * 1.15
    au1 = sa1 - s1
    inf1 = sa1 * 0.962
    print (f'o salario antes era {s1} o percentual aplicado foi 15% o valor do aumento foi {au1} o novo salario apos o aumento é {sa1}  o valor descontado a inflaçao é {inf1}')


elif s1 > 700.00 and s1 < 1500.00:
     sa1 = s1 * 1.10
     au1 = sa1 - s1
     inf1 = sa1 * 0.962
     print (f'o salario antes era {s1} o percentual aplicado foi 10% o valor do aumento foi {au1} o novo salario apos o aumento é {sa1}  o valor descontado a inflaçao é {inf1}')
   
elif s1 > 1500.00:
     sa1 = s1 * 1.05
     au1 = sa1 - s1
     inf1 = sa1 * 0.962
     print (f'o salario antes era {s1} o percentual aplicado foi 5% o valor do aumento foi {au1} o novo salario apos o aumento é {sa1} 5 o valor descontado a inflaçao é {inf1}')