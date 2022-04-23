// Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.
// TC: O(n) / SC: O(n)

func numUniqueEmails(emails []string) int {
    set := make(map[string]bool)
    
    for _, email := range emails {
        parts := strings.Split(email, "@")
        // fmt.Println(parts)
        local := strings.Split(parts[0], "+")
        check := strings.Replace(local[0], ".", "", -1) + "@" + parts[1]
        set[check] = true
    }
    
    return len(set)
}