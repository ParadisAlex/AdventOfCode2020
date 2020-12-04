class Credential:
    birth_year = ''
    issue_year = ''
    expiration_year = ''
    height = ''
    hair_color = ''
    eye_color = ''
    passport_id = ''
    country_id = ''

    def __init__(self, to_parse):
        self.parse_input(to_parse)

    def parse_input(self, to_parse):
        lines = to_parse.split(' ')
        lines = list(filter(None, lines))
        for line in lines:
            prefix = line.split(':')[0].strip()
            val = line.split(':')[1].strip()
            # python be like "what is a switch/case yo? Shits wild dawg...
            if prefix == 'byr':
                self.birth_year = val.strip()
            elif prefix == 'iyr':
                self.issue_year = val.strip()
            elif prefix == 'eyr':
                self.expiration_year = val.strip()
            elif prefix == 'hgt':
                self.height = val.strip()
            elif prefix == 'hcl':
                self.hair_color = val.strip()
            elif prefix == 'ecl':
                self.eye_color = val.strip()
            elif prefix == 'pid':
                self.passport_id = val.strip()
            elif prefix == 'cid':
                self.country_id = val.strip()

    def is_valid(self):
        if self.birth_year and self.issue_year and self.expiration_year and self.height and self.hair_color and self.eye_color and self.passport_id:
            return True
        else:
            return False

    def is_extra_valid(self):
        byr_check = False
        iyr_check = False
        eyr_check = False
        hgt_check = False
        hcl_check = False
        ecl_check = False
        pid_check = False
        eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if self.birth_year:
            if 1920 <= int(self.birth_year) <= 2002:
                byr_check = True
        if self.issue_year:
            if 2010 <= int(self.issue_year) <= 2020:
                iyr_check = True
        if self.expiration_year:
            if 2020 <= int(self.expiration_year) <= 2030:
                eyr_check = True
        if self.height:
            if self.height[-2:] == 'in' and (59 <= int(self.height.replace('in', '')) <= 76):
                hgt_check = True
            if self.height[-2:] == 'cm' and (150 <= int(self.height.replace('cm', '')) <= 193):
                hgt_check = True
        if self.hair_color:
            if self.hair_color[0] == '#' and len(self.hair_color[1:]) == 6 and self.hair_color[1:].isalnum():
                hcl_check = True
        if self.eye_color in eye_colors:
            ecl_check = True
        if self.passport_id:
            if len(self.passport_id) == 9 and self.passport_id.isdigit():
                pid_check = True

        if byr_check and iyr_check and eyr_check and hgt_check and hcl_check and ecl_check and pid_check:
            return True
        else:
            return False

    def print(self):
        print("byr:{}, iyr:{}, eyr:{}, hgt:{} hcl:{} ecl:{} pid:{} cid:{}".format(
            self.birth_year,
            self.issue_year,
            self.expiration_year,
            self.height,
            self.hair_color,
            self.eye_color,
            self.passport_id,
            self.country_id
        ))
