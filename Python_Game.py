import random
import time
num=0

def enemy1():
  print("（V) ∧∧ (V)")
  print("  ヽ(･ω･)ﾉ")
  print("   /  /")
  print("  ノ￣ゝ")
  print("バルタン星人が現れた!!")
  return 100,30

def enemy2():
  print("  ／⌒＼")
  print("（´･ω･`）")
  print("《《《《")
  print("  》》》")
  print("  《《")
  print("    》")
  print("ホイミが現れた")
  return 200,10

def enemy3():
  print("           ヽ￣￣~ヽ")
  print("            )´・ω・｀)")
  print("           / つ つ")
  print("     ,～'｀ﾉ     /")
  print("    ﾉ ｀､´＿＿ノ")
  print("  ﾉ _ノ ~")
  print("'´~")
  print("一旦木綿が現れた")
  return 1,1

Player_HP=200
Player_ATK=40
Player_DAMAGE=0
a=1

enemy_DAMAGE=0
while a==1:
  while Player_DAMAGE < Player_HP:
    enemy_type=int(random.randrange(start=1, stop=4))
    if enemy_type==1:
      num=enemy1()
    elif enemy_type==2:
      num=enemy2()
    else:
      num=enemy3()

    while Player_DAMAGE < Player_HP:
      print("playerのターン")
      action=int(input("1:攻撃  0:逃げる  "))
      if action == 1:
        print("playerの攻撃! {}のダメージ".format(Player_ATK))
        enemy_DAMAGE=enemy_DAMAGE+Player_ATK
        if enemy_DAMAGE >= num[0]:
          print("enemyは倒れた")
          print("   ⊂⊃")
          print("  ∧＿∧")
          print("（´･ω･`）")
          print("   ) )")
          print("   y")
          print("playerの勝ちです!!")
          enemy_DAMAGE=0
          time.sleep(1)
          print("新たな敵が現れた!")
          break
      else:
        print("playerは逃げた")
        break
      print("enemyのターン")
      print("enemyの攻撃! {}のダメージ".format(num[1]))
      Player_HP=Player_HP-num[1]
      print("PlayerのHP:{}".format(Player_HP))

  print("playerは死んでしまった")
  life=int(input("冒険を続けますか？ 1:続ける  0:終了する  "))
  if life==1:
    Player_HP=200
    enemy_DAMAGE=0
  else:
    break
