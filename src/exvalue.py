import exercises

#  sh_v, ar_v, ch_v, ba_v, le_v, co_v, corr_v, ca_v

class Value:
    def get_value(self):

        for j, i in self.items():
            shoulder_vol = 0
            arms_vol = 0
            chest_vol = 0
            back_vol = 0
            legs_vol = 0
            core_vol = 0
            corrective_vol = 0
            cardio_vol = 0
            # for i in self.values():
            for x in range(len(i)):
                for sh_v, v in exercises.shoulders_val.items():
                    if i[x] == sh_v:
                        shoulder_vol += v
                for ar_v, v in exercises.arms_val.items():
                    if i[x] == ar_v:
                        arms_vol += v        
                for ch_v, v in exercises.chest_val.items():
                    if i[x] == ch_v:
                        chest_vol += v
                for ba_v, v in exercises.back_val.items():
                    if i[x] == ba_v:
                        back_vol += v
                for le_v, v in exercises.legs_val.items():
                    if i[x] == le_v:
                        legs_vol += v
                for co_v, v in exercises.core_val.items():
                    if i[x] == co_v:
                        core_vol += v
                for corr_v, v in exercises.corrective_val.items():
                    if i[x] == corr_v:
                        corrective_vol += v
                for ca_v, v in exercises.cardio_val.items():
                    if i[x] == ca_v:
                        cardio_vol += v
            day = {j : [shoulder_vol, arms_vol, chest_vol, back_vol, legs_vol, core_vol, corrective_vol, cardio_vol]}
            return day
        # return shoulder_vol, arms_vol, chest_vol, back_vol, legs_vol, core_vol, corrective_vol, cardio_vol
                        
        # return print(shoulder_vol, arms_vol, chest_vol, back_vol, legs_vol, core_vol, corrective_vol, cardio_vol)
            #     print(x)
            #     print(i)
