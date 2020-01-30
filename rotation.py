import json

def main():

	#GET ALPHABET
	#READ FILE
	Fconfig = open('config.json', 'r')
	data=Fconfig.read()

	#PARSE FILE
	obj = json.loads(data)
	abc = str(obj['alphabet_low'])
	ABC = str(obj['alphabet_up'])

	#STRING INPUT
	print("Text input: ")
	text = str(input())


	#MAIN
	for i in range(len(abc)):			#possible rotations
		print("\nN = " + str(i) + "\t")
		line_output = ""

		for j in range(len(text)):		#loop input letter
			found = False

			for k in range(len(abc)):	#compare to letter in alphabet

				if(text[j]==abc[k]):	#if match lowercase letter rotate i positions in alphabet
					n = k+i
					if(n >= len(abc)): 	#loop alphabet
						n -= len(abc)
					line_output+=abc[n]
					found=True
					break

				elif (text[j]==ABC[k]):	#if match uppercase letter rotate i positions in alphabet
					n = k+i
					if(n >= len(abc)): 	#loop alphabet
						n -= len(abc)
					line_output+=ABC[n]
					found=True
					break

			if (found == False):		#If not in alphabet keep same character
				line_output+=text[j]

		print(line_output)
	

if __name__ == "__main__":
    main()
