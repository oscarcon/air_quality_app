#include <iostream>
#include <algorithm>
#include <boost/array.hpp>
#include <boost/asio.hpp>
#include <boost/thread.hpp>
using boost::asio::ip::tcp;

void sock_read_handler(tcp::socket *socket, boost::array<char, 256> *buf, size_t bytes) {
	std::cout.write(buf->c_array(), bytes);
	std::cout << std::flush;
	// std::cout << "read handler" << std::endl;
	// std::cout << buf->c_array() << std::endl;
	socket->async_read_some(boost::asio::buffer(buf, 256), boost::bind(sock_read_handler, socket, buf, boost::asio::placeholders::bytes_transferred));
}
void sock_write_handler(tcp::socket *socket, boost::array<char, 256> *buf, const boost::system::error_code &e, size_t bytes) {
	// std::cout << "write handler" << std::endl;
	// std::cout << e.message() << std::endl;
	buf->assign(0);
	// std::fflush(stdin);
}
void write_sock(tcp::socket *socket, boost::array<char, 256> *buf, size_t len) {
	// std::cout << "Sendding" << std::endl;
	socket->async_write_some(boost::asio::buffer(buf, len), boost::bind(sock_write_handler, socket, buf, boost::asio::placeholders::error , boost::asio::placeholders::bytes_transferred));
}
void write_thread(boost::asio::io_context *io_context, tcp::socket *socket) {
	for (;;) {
		// std::cout << "Input thread " << std::endl;
		boost::array<char, 256> *buf = new boost::array<char, 256>();
		std::cin.getline(buf->c_array(), 255);
		int len = std::strlen(buf->c_array());
		(*buf)[len++] = '\n';
		// std::cout << "It's ok! "  << buf->c_array() << std::endl;
		boost::asio::post(*io_context, boost::bind(write_sock, socket, buf, len));
	}
}
void empty_handler(const boost::system::error_code &e) {
	// std::cout << e.message() << std::flush;
}
void keep_connection(tcp::socket *socket, boost::asio::steady_timer *wdt) {
	socket->async_write_some(boost::asio::buffer("", 1), boost::bind(empty_handler, boost::asio::placeholders::error));
	wdt->expires_from_now(std::chrono::seconds(2));
	wdt->async_wait(boost::bind(keep_connection, socket, wdt));
}
int main(int argc, char **argv) {
	try {
		if (argc != 3) {
			std::cerr << "Usage: socket_app <host> <port>" << std::endl;
			return 1;
		}
		boost::array<char, 256> *buf2 = new boost::array<char, 256>();
		boost::asio::io_context io_context;
		tcp::resolver resolver(io_context);
		tcp::resolver::results_type endpoints = resolver.resolve(argv[1], argv[2]);
		tcp::socket socket(io_context);
		boost::asio::connect(socket, endpoints);
		boost::thread t(boost::bind(write_thread, &io_context, &socket));
		socket.async_read_some(boost::asio::buffer(buf2, 256), boost::bind(sock_read_handler, &socket, buf2, boost::asio::placeholders::bytes_transferred));
		boost::asio::steady_timer wdt(io_context, boost::asio::chrono::seconds(2));
		wdt.async_wait(boost::bind(keep_connection, &socket, &wdt));
		io_context.run();
		t.join();
	}
	catch (std::exception &e) {
			std::cerr << e.what() << std::endl;
	}
	return 0;
}