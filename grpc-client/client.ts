import { HelloWorldServiceClient } from "./generated/helloworld/v1/service.client";
import { ChannelCredentials } from "@grpc/grpc-js";
import { GrpcTransport } from "@protobuf-ts/grpc-transport";
import type { HelloWorldRequest } from "./generated/helloworld/v1/service";

class GrpcClient {
  client: HelloWorldServiceClient;

  constructor() {
    const transport = new GrpcTransport({
      host: "localhost:5001",
      channelCredentials: ChannelCredentials.createInsecure(),
    });
    this.client = new HelloWorldServiceClient(transport);
  }

  helloWorld = async () => {
    const request: HelloWorldRequest = {
      name: "Bun client"
    };
    const call = this.client.helloWorld(request);
    const response = await call.response;
    console.log(`Response: ${response.result}`)
  };
}

export { GrpcClient };
