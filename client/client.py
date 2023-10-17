import grpc
import image_search_pb2
import image_search_pb2_grpc

# Create the gRPC channel with the max message size set to 10 MB
channel = grpc.insecure_channel('localhost:3080', options=[('grpc.max_receive_message_length', 10 * 1024 * 1024)])

def run():
    # Connect to the gRPC server
    with grpc.insecure_channel('localhost:3080') as channel:
        stub = image_search_pb2_grpc.ImageSearchServiceStub(channel)

        # Prompt the user to enter a query
        query = input('Enter a query: ')

        # Send a request to search for an image
        response = stub.SearchImage(image_search_pb2.ImageRequest(keyword=query))

        # Save the image to a file
        with open('image.jpg', 'wb') as image_file:
            image_file.write(response.image_data)

if __name__ == '__main__':
    run()
