def get_rank(card):
	rank=card[0]
	ranks={'T':10,'J':11,'Q':12,'K':13,'A':14}
	if rank in ranks:
		return ranks[rank]
	else:
		return int(rank)

def sort_hand(hand):
	return sorted(hand,key=get_rank)

def split_hand(hand):
	kinds=[card[0] for card in hand]
	types=[card[1] for card in hand]
	return (kinds,types)

def is_same_type(types):
	if len(set(types))==1:
		return True
	return False

def is_royal_flush(kinds,types):
	kinds_ok=False
	if kinds[0]=='T' and kinds[1]=='J' and kinds[2]=='Q' and kinds[3]=='K' and kinds[4]=='A':
		kinds_ok=True
	if kinds_ok and is_same_type(types):
		return True
	return False

def is_straight_flush(kinds,types):
	ranks=[get_rank(kind) for kind in kinds]
	is_consecutive=False
	if ranks[1]==ranks[0]+1 and ranks[2]==ranks[1]+1 and ranks[3]==ranks[2]+1 and ranks[4]==ranks[3]+1:
		is_consecutive=True
	if is_consecutive and is_same_type(types):
		return True
	return False

def is_four_of_a_kind(kinds,types):
	if (kinds[0]==kinds[1]==kinds[2]==kinds[3]) or (kinds[1]==kinds[2]==kinds[3]==kinds[4]):
		return True
	return False

def is_full_house(kinds,types):
	if ((kinds[0]==kinds[1]) and (kinds[2]==kinds[3]==kinds[4])) or ((kinds[0]==kinds[1]==kinds[2]) and (kinds[3]==kinds[4])):
		return True
	return False

def is_flush(kinds,types):
	return is_same_type(types)

def is_straight(kinds,types):
	ranks=[get_rank(kind) for kind in kinds]
	if ranks[1]==ranks[0]+1 and ranks[2]==ranks[1]+1 and ranks[3]==ranks[2]+1 and ranks[4]==ranks[3]+1:
		return True
	return False

def is_three_of_a_kind(kinds,types):
	if (kinds[0]==kinds[1]==kinds[2]) or (kinds[1]==kinds[2]==kinds[3]) or (kinds[2]==kinds[3]==kinds[4]):
		return True
	return False

def is_two_pairs(kinds,types):
	if (kinds[1]==kinds[2] and kinds[3]==kinds[4]) or (kinds[0]==kinds[1] and kinds[3]==kinds[4]) or (kinds[0]==kinds[1] and kinds[2]==kinds[3]):
		return True
	return False

def is_one_pair(kinds,types):
	if kinds[0]==kinds[1] or kinds[1]==kinds[2] or kinds[2]==kinds[3] or kinds[3]==kinds[4]:
		return True
	return False

def two_pairs_tie_helper(kinds,types):
	if kinds[1]==kinds[2] and kinds[3]==kinds[4]:
		return (sorted([get_rank(kinds[1]),get_rank(kinds[3])]),get_rank(kinds[0]))
	elif kinds[0]==kinds[1] and kinds[3]==kinds[4]:
		return (sorted([get_rank(kinds[0]),get_rank(kinds[3])]),get_rank(kinds[2]))
	else:
		return (sorted([get_rank(kinds[0]),get_rank(kinds[2])]),get_rank(kinds[4]))

def one_pair_tie_helper(kinds):
	if kinds[0]==kinds[1]:
		return get_rank(kinds[0])
	elif kinds[1]==kinds[2]:
		return get_rank(kinds[1])
	elif kinds[2]==kinds[3]:
		return get_rank(kinds[2])
	else:
		return get_rank(kinds[3])

def find_winner(handA,handB):
	sorted_handA=sort_hand(handA)
	sorted_handB=sort_hand(handB)
	kinds_A,types_A=split_hand(sorted_handA)
	kinds_B,types_B=split_hand(sorted_handB)
	
	#royal flush[no tie in this case]
	royal_flush_A=is_royal_flush(kinds_A,types_A)
	royal_flush_B=is_royal_flush(kinds_B,types_B)
	if  royal_flush_A and not royal_flush_B:
		return 1
	elif not royal_flush_A and royal_flush_B:
		return 2
		
	#straight flush
	straight_flush_A=is_straight_flush(kinds_A,types_A)
	straight_flush_B=is_straight_flush(kinds_B,types_B)
	if straight_flush_A and not straight_flush_B:
		return 1
	elif not straight_flush_A and straight_flush_B:
		return 2
	elif straight_flush_A and straight_flush_B:
		if int(kinds_A[0])>int(kinds_B[0]):
			return 1
		else:
			return 2

	#four of a kind
	four_of_a_kind_A=is_four_of_a_kind(kinds_A,types_A)
	four_of_a_kind_B=is_four_of_a_kind(kinds_B,types_B)
	if four_of_a_kind_A and not four_of_a_kind_B:
		return 1
	elif not four_of_a_kind_A and four_of_a_kind_B:
		return 2
	elif four_of_a_kind_A and four_of_a_kind_B:
		val_A=int(get_rank(kinds_A[0]))
		if kinds_A[3]==kinds_A[4]:
			val_A=int(get_rank(kinds_A[4]))
		val_B=int(get_rank(kinds_B[0]))
		if kinds_B[3]==kinds_B[4]:
			val_B=int(gt_rank(kinds_B[4]))
		if val_A>val_B:
			return 1
		else:
			return 2

	#full house [Check tie condition]
	full_house_A=is_full_house(kinds_A,types_A)
	full_house_B=is_full_house(kinds_B,types_B)
	if full_house_A and not full_house_B:
		return 1
	elif not full_house_A and full_house_B:
		return 2
	elif full_house_A and full_house_B:
		
		pair_A=get_rank(kinds_A[3])
		three_A=get_rank(kinds_A[0])
		if kinds_A[0]==kinds_A[1] and kinds_A[2]==kinds_A[3]==kinds_A[4]:
			pair_A=get_rank(kinds_A[0])
			three_A=get_rank(kinds_A[2])

		pair_B=get_rank(kinds_B[3])
		three_B=get_rank(kinds_B[0])
		if kinds_B[0]==kinds_B[1] and kinds_B[2]==kinds_B[3]==kinds_B[4]:
			pair_B=get_rank(kinds_B[0])
			three_B=get_rank(kinds_B[2])

		if three_A>three_B:
			return 1
		elif three_A<three_B:
			return 2
		else:
			if pair_A>pair_B:
				return 1
			else:
				return 2

	#Flush
	flush_A=is_flush(kinds_A,types_A)
	flush_B=is_flush(kinds_B,types_B)
	if flush_A and not flush_B:
		return 1
	elif not flush_A and flush_B:
		return 2
	elif flush_A and flush_B:
		for idx in range(4,-1,-1):
			if get_rank(kinds_A[idx])>get_rank(kinds_B[idx]):
				return 1
			elif get_rank(kinds_B[idx])>get_rank(kinds_B[idx]):
				return 2


	#straight
	straight_A=is_straight(kinds_A,types_A)
	straight_B=is_straight(kinds_B,types_B)
	if straight_A and not straight_B:
		return 1
	elif not straight_A and straight_B:
		return 2
	elif straight_A and straight_B:
		val_A=get_rank(kinds_A[4])
		val_B=get_rank(kinds_B[4])
		if val_A>val_B:
			return 1
		else:
			return 2

	#three of a kind
	three_oak_A=is_three_of_a_kind(kinds_A,types_A)
	three_oak_B=is_three_of_a_kind(kinds_B,types_B)
	if three_oak_A and not three_oak_B:
		return 1
	elif not three_oak_A and three_oak_B:
		return 2
	elif three_oak_A and three_oak_B:
		val_A=get_rank(kinds_A[2])
		if kinds_A[0]==kinds_A[1]==kinds_A[2]:
			val_A=get_rank(kinds_A[0])
		elif kinds_A[1]==kinds_A[2]==kinds_A[3]:
			val_A=get_rank(kinds_A[1])
		val_B=get_rank(kinds_B[2])
		if kinds_B[0]==kinds_B[1]==kinds_B[2]:
			val_B=get_rank(kinds_B[0])
		elif kinds_B[1]==kinds_B[2]==kinds_B[3]:
			val_B=get_rank(kinds_B[1])
		if val_A>val_B:
			return 1
		else: 
			return 2
	
	#two pairs [complicated tie case]
	two_pairs_A=is_two_pairs(kinds_A,types_A)
	two_pairs_B=is_two_pairs(kinds_B,types_B)
	if two_pairs_A and not two_pairs_B:
		return 1
	elif not two_pairs_A and two_pairs_B:
		return 2
	elif two_pairs_A and two_pairs_B:
		list_A,other_A=two_pairs_tie_helper(kinds_A)
		list_B,other_B=two_pairs_tie_helper(kinds_B)
		if list_A[1]>list_B[1]:
			return 1
		elif list_B[1]>list_A[1]:
			return 2
		else:
			if list_A[0]>list_B[0]:
				return 1
			elif list_B[0]>list_A[0]:
				return 2
			else:
				if other_A>other_B:
					return 1
				else:
					return 2

	#one pair
	one_pair_A=is_one_pair(kinds_A,types_A)
	one_pair_B=is_one_pair(kinds_B,types_B)
	if one_pair_A and not one_pair_B:
		return 1
	elif not one_pair_A and one_pair_B:
		return 2
	elif one_pair_A and one_pair_B:
		pair_A=one_pair_tie_helper(kinds_A)
		pair_B=one_pair_tie_helper(kinds_B)
		if pair_A>pair_B:
			return 1
		elif pair_A<pair_B:
			return 2
		else:
			for idx in range(4,-1,-1):
				if get_rank(kinds_A[idx])>get_rank(kinds_B[idx]):
					return 1
				elif get_rank(kinds_A[idx])<get_rank(kinds_B[idx]):
					return 2
	
	#high card
	for idx in range(4,-1,-1):
		if get_rank(kinds_A[idx])>get_rank(kinds_B[idx]):
			return 1
		elif get_rank(kinds_A[idx])<get_rank(kinds_B[idx]):
			return 2

def read_from_file():
	win_A=0
	with open("poker.txt") as f:
		for line in f:
			cards=line.strip().split(' ')
			handA=cards[0:5]
			handB=cards[5:10]
			print(handA,handB)
			if find_winner(handA,handB)==1:
				win_A=win_A+1
	print(win_A)
read_from_file()
