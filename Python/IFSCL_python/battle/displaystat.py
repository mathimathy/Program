class DisplayStat:
    def display(self, lg, monster):
        #lyoko guerrier
        for chr in lg:
            lg_text=f"{chr.name}\nHP: {chr.hp}\nSP: {chr.mana}\n-----"
            print(lg_text)
        for m in monster:
            m_text=f"{m.name}\nHP: {m.hp}\n\n-----"
            print(m_text)