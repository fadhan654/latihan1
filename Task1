public class Books {
    private String author;
    private String title;
    private double price;
    private int publisherNumber;

    public Books(String author, String title, double price, int publisherNumber) {
        this.author = author;
        this.title = title;
        this.price = price;
        this.publisherNumber = publisherNumber;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public int getPublisherNumber() {
        return publisherNumber;
    }

    public void setPublisherNumber(int publisherNumber) {
        this.publisherNumber = publisherNumber;
    }

    public static void main(String[] args) {
        Books book1 = new Books("John Doe", "Java Programming", 29.99, 12345);
        Books book2 = new Books("Jane Smith", "Introduction to Algorithms", 39.99, 54321);
        double totalPrice = book1.getPrice() + book2.getPrice();
        System.out.println("Total price for all books: $" + totalPrice);
    }
}
