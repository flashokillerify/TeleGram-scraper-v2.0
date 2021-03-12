with open('BanNumbers.csv', 'r') as f:
	banned_numbers = f.read().split('\n')

with open('phone.csv', 'r') as f:
	existing_numbers = f.read().split('\n')

for b_num in banned_numbers:
	if b_num in existing_numbers:
		existing_numbers.remove(b_num)

with open('phone.csv', 'w') as f:
	f.write('\n'.join(existing_numbers))

print ("[INFO] Removed banned numbers from phone.csv")