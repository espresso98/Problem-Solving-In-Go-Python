func capitalizeTitle(title string) string {
	words := strings.Split(strings.ToLower(title), " ")
	// fmt.Println(words)
	for i, word := range words {
		if len(word) > 2 {
			words[i] = strings.ToUpper(string(word[0])) + word[1:]
			// fmt.Printf("word[0]: %T, word: %T\n", word[0], word)
		}
	}
	capitalized := strings.Join(words, " ")
	return capitalized
}
